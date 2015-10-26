"""Script to get build information from Jenkins"""
import sys
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def main():
    """Main entry point for the script."""
    #releases = get_recent_release_job_information(URL)
    server=get_server_instance()
    print "Jenkins Version:"
    print server.version

    #get_job_details()

    print jenkinsapi.api.get_view_from_url('http://jenkins-master-ux.awsdev.usatoday.com/view/Build/')

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