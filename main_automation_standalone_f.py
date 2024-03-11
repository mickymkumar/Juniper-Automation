"""
Title: Standalone Automation
Author: Micky Kumar
"""
import os, datetime
import subprocess
import yaml

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
class JuniperAutomation():
    def  __init__(self, hostname):
        self.config_file = 'config.yaml'
        self.config = load_config(self.config_file)
        pass
    # Add any configurations

    def BuildImage(self):
        #get the images from image location
        #build  an image using dockerfile in that directory
        image = self.config['other']['image']
        os.system(image)
        pass
    
    def BuildHelm(self):
  
        #build helm  charts from Internal Helm repository.
        helm = self.config['other']['helm']
        os.system(helm)
        pass

    def DeployPMN():
        
        pass
       # install package AWScli, PyYaml, botocore, s3transfer, coloroma, rsa, urllib3, pyasn1, six
        def install_package():
            packages = ['AWScli', 'PyYaml', 'botocore', 's3transfer', 'coloroma', 'rsa', 'urllib3', 'pyasn1', 'six']
            os.system('apt-get {package}')
            pass
       # apt-get update
        def update():
            os.system("apt-get update")
            pass
       # Configure AWS CLI from configs settings
        def configure_aws():
            os.system('aws configure set {self.config['PMN']['aws_access_key_id']} ')
            os.system('aws configure set {self.config['PMN']['aws_secret_access_key']} ')
            os.system('aws configure set {self.config['PMN']['region']}')
            os.system('aws configure set {self.config['PMN']['role_arn']}')
            os.system('aws configure set {self.config['PMN']['source_profile']}')
            pass
       # Update aws eks update-kubeconfig  with name of pmn-dev and region is region us-west-2
        def update_eks():
            os.system(f'aws eks update-kubeconfig --name pmn-dev --region us-west-2')
            pass
       # terform init
        def terraform_init():
            os.system("terraform init")
            pass
       # terraform apply 
        def  terraform_apply():
            os.system("terraform apply")
            pass
 
    def DeployAGW(): #Based on Docker 
        #git clone AGW repo
        def clone_AGW():
            os.system("git clone https://github.com/wavelabsai/pmn-systems")
            print(" git AGW Cloned")
            pass
        #cd to cloned folder
        def cd_to_cloned_folder():
            os.system("cd ~/pmn-systems/lte/gateway")

            pass
        #terraform init 
        def  tf_init():
            os.system("terraform init")
        #Copy your rootCA.pem
            def copy_rootca():
                os.system("mkdir -p /var/opt/magma/certs")
                os.system("vim /var/opt/magma/certs/rootCA.pem")
                pass
        # Run AGW installation
            def agw_installation():
                os.system('cd /lte/gateway/deploy/')
                os.system('bash agw_install_docker.sh')
                pass
        # Start your access gateway
            def  start_agw():
                os.system('cd /var/opt/magma/docker')
                os.system('sudo docker-compose up -d')
                pass
        # Get Hardware ID and Challenge key and add AGW in your orc8r.
            def hardware_challenge():
                os.system('docker exec magmad show_gateway_info.py')
                pass
        #restart your access gateway
            def  restart_agw():
                os.system('sudo docker-compose up -d --force-recreate')
                pass

        pass

    def  RunTests():
    # run test cases using main
        os.system("git clone https://github.com/mickymkumar/Juniper-Automation")
        os.system('cd Juniper-Automation ')
        os.system('cd test script/frontend/')
        os.system('py main.py')

        pass

