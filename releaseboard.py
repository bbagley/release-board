"""Script to get build information from Jenkins"""
import sys
import jenkinsapi

def main():
    """Main entry point for the script."""
    #releases = get_recent_release_job_information(URL)
    pass


def get_recent_release_job_information(url):
    """Return a list PROD release jobs with associated versions."""
    pass

def get_latest_build_information(url):
    """Return a list build jobs with recent versions and success or failure."""
    pass

if __name__ == '__main__':
    sys.exit(main())