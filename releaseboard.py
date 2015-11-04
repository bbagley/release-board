"""Script to get build information from Jenkins"""
import sys
from json import JSONEncoder
import jenkins

def main():
    """Main entry point for the script."""
    server = jenkins.Jenkins('http://jenkins-master-ux.awsdev.usatoday.com')
    version = server.get_version()
    print version

    #views = server.get_views()
    #print views

    #prodjobs = server.get_job_info_regex('_to_production')
    #print prodjobs

    jobs = server.get_all_jobs()
    #print jobs
    prodJobs = {}

    for job in jobs:
        #print job['fullname']
        if '_to_production' in job['fullname']:
            paper = job['fullname'].split("_")[0]
            print paper
            prodJobs.update({paper : job})

    print prodJobs
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