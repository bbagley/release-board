"""Script to get build information from Jenkins"""
import sys
from json import JSONEncoder
import jenkins

sitelist = { "baxterbulletin", "argusleader", "battlecreekenquirer", "clarionledger","blackmountainnews","coshoctontribune","delmarvanow","floridatoday","greatfallstribune","greenvilleonline","hattiesburgamerican","ithacajournal","jconline","jacksonsun","mansfieldnewsjournal","marionstar","postcrescent","poughkeepsiejournal","press-citizen","sheboyganpress","shreveporttimes","thecalifornian","thedailyjournal","thehammontonnews","theleafchronicle","thenews-messenger","wisconsinrapidstribune","zanesvilletimesrecorder","thespectrum","thestarpress","thetimesherald","thetowntalk","thenorthwestern","visaliatimesdelta","wausaudailyherald","tallahassee","theadvertiser","thenewsstar","stargazette","statesmanjournal","stevenspointjournal","reno","rgj","sctimes","pnj","portclintonnewsherald","pressconnects","news-press","packersnews","pal-item","newarkadvocate","news-leader","newsleader","montgomeryadvertiser","mycentraljersey","livingstondaily","marcoislandflorida","marshfieldnewsherald","lancastereaglegazette","lansingstatejournal","lavozarizona","hawkcentral","hometownlife","htrnews","fsunews","greenbaypressgazette","guampdn","elsoldesalinas","farmersadvance","fdlreporter","dmjuice","dnj","desertsun","delawareonline","dailyrecord","dailyworld","citizen-times","coloradoan","courierpostonline","app","bucyrustelegraphforum","desmoinesregister","lohud","alamogordonews","currentargus","daily-times","demingheadlight","elpasotimes","elpasoymas","lcsun-news","ruidosonews","scsun-news","tennessean","democratandchronicle","burlingtonfreepress","centralfloridafuture","chillicothegazette","courier-journal","cincinnati","freep","indystar" }

def main():
    """Main entry point for the script."""
    server = jenkins.Jenkins('http://jenkins-master-ux.awsdev.usatoday.com')
    version = server.get_version()
    print version

    jobs = server.get_all_jobs()
    #print jobs
    prodJobs = {}

    for job in jobs:
        #print job['fullname']
        if '_to_production' in job['fullname']:
            paper = job['fullname'].split("_")[0]
            #print paper
            jobinfo = server.get_job_info(job['fullname'])
            #print jobinfo
            prodJobs.update({paper : job})

    #print prodJobs

    bax = server.get_job_info("baxterbulletin_to_production")
    print bax
    pass

def get_server_instance():
    jenkins_url = 'http://jenkins-master-ux.awsdev.usatoday.com/'
    server = Jenkins(jenkins_url)
    return server

def get_recent_release_job_information(url):
    """Return a list PROD release jobs with associated versions."""
    pass

def get_latest_build_information(url):
    """Return a list build jobs with recent versions and success or failure."""
    pass

"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print 'Job Name:%s' %(job_instance.name)
        print 'Job Description:%s' %(job_instance.get_description())
        print 'Is Job running:%s' %(job_instance.is_running())
        print 'Is Job enabled:%s' %(job_instance.is_enabled())

if __name__ == '__main__':
    sys.exit(main())