"""
Title: Standalone Automation
Author: Micky Kumar
"""

class JuniperAutomation():
    def  __init__(self, hostname):
        pass
    # Add any configurations

    def BuildImage():
        #get the images from image location
        #build  an image using dockerfile in that directory
        pass
    
    def BuildHelm():
        #build helm  charts from Internal Helm repository.
        pass

    def DeployPMN():
        
        pass
       # install package AWScli, PyYaml, botocore, s3transfer, coloroma, rsa, urllib3, pyasn1, six
       # apt-get update & 
       # Configure AWS CLI from configs settings
       # Update aws eks update-kubeconfig  with name of pmn-dev and region is region us-west-2
       # terform init
       # terraform apply 
 
    def DeployAGW(): #Based on Docker 
        #git clone AGW repo
        #cd to cloned folder
        #terraform init 
        #Copy your rootCA.pem
        # Run AGW installation
        # Start your access gateway
        # Get Hardware ID and Challenge key and add AGW in your orc8r
        #restart your access gateway


        pass

    def  RunTests():
        pass
    # run test cases using main