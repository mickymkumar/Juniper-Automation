"""
Title: Standalone for Juniper Automation
Date:  2024-02-05
Author: Micky Kumar


"""
import os


class main():
    def __init__(self):
        pass

    def latest_code():
      os.system("sudo git clone https://github.com/wavelabsai/pmn-systems.git")
      print("\nclone latest code updated\n")
       
    def Update_package():
       os.system("sudo apt update")
       print("\nPackage updated\n")
    
    def run_gateway():
      def copy_rootCA():
          os.system(" cp /magma/orc8r/rootCA.pem /var/opt/magma/certs/rootCA.pem")
          print("\nPackage updated\n")

      def docker_install():
          os.system(" cp https://github.com/wavelabs/pmn-system/raw/v1.8/lte/gateway/deploy/agw_install_docker.sh /tmp/agw_install_docker.sh")
          print("\n copy docker updated\n")

      def run_AGW():
          os.system("sudo -i /tmp/agw_install_docker.sh")
          print("\n run AGW updated\n")

      def Create_control_proxy():    
          os.system(" sudo vi /var/opt/magma/configs/control_proxy.yml")
          os.system("\n cloud_address: controller.orc8r.magmacore.link \n"
                    + "\n cloud_port: 443\n"
                    + "\n bootstrap_address: bootstrapper-controller.orc8r.magmacore.link \n"
                    +  "\n bootstrap_port: 443\n"
                    + "\n fluentd_address: fluentd.orc8r.magmacore.link \n"
                    + "\n  fluentd_port: 24224 \n"      
                    + "\n rootca_cert: /var/opt/magma/certs/rootCA.pem \n"             
                    )              
         
          print("\n created control_proxy updated\n")
      def Start_AGW():  
         os.system("cd /var/opt/magma/docker && sudo docker-compose up -d")
         print("\n AGW started\n")

      def harware_ID_challenge_key():
         os.system("docker exec magmad show_gateway_info.py")
         print("\n showed Get Hardware ID and Challenge key \n")            

      def restart_AGW():
         os.system("cd /var/opt/magma/docker && sudo docker-compose up -d --force-recreate")
         print("\n restarted AGW \n") 

      def create_dir_cert():
         os.system("cd ~/secrets/certs")
         print("\n restarted AGW \n") 

      def move_certificates ():
         os.system("cp  /var/opt/magma/certs/controller.crt ${MAGMA_ROOT}/orc8r/cloud/deploy/scripts/self_sign_certs.sh {{ gatewayip }}"
                    +"cp /var/opt/magma/certs/controller.crt  ~/secrets/certs/.crt controller.crt"
                    + "cp /var/opt/magma/certs/controller.crt ~/secrets/certs/{{ gatewayip }}.key controller.key"
                    + "cp /var/opt/magma/certs/rootCA.pem  ~/secrets/certs/rootCA.pem "
                    + "cp /var/opt/magma/certs/rootCA.pem ${MAGMA_ROOT}/orc8r/cloud/deploy/scripts/create_application_certs.sh {{ gatewayip }}"
                  )
         print("\n moved certificates \n") 

      def Create_admin_operator():
         os.system("openssl pkcs12 -export -inkey admin_operator.key.pem -in admin_operator.pem -out admin_operator.pfx")
         os.system("echo {input("Enter Export Password: ")}")
         os.system("echo {input("Verifying - Enter Export Password: ")}")
         print("\n created admin operator \n")
         
      def display_cert():
         os.system("ls -1 ~/secrets/certs/")
         print("\n displayed certs \n")

      def Initialize_Terraform():
         os.system("terraform init /orc8r/cloud/deploy/terraform/MODULE?ref=v1.8")
         print("\n Initialized Terraform \n")

      def Terraform_Apply_infra():
         os.system("terraform apply -target=module.orc8r")
         print("\n Terraform Applied for Infrastructure \n")      

      def Terraform_Apply_secert():
         os.system('terraform apply -target=module.orc8r-app.null_resource.orc8r_seed_secrets')
         print("\n Terraform Applied for Secrets \n") 

      def Terraform_Apply_App():
         os.system('terraform apply /orc8r/cloud/deploy/terraform/MODULE?ref=v1.8')
         print("\n Terraform Applied for Application \n")          

      def Create_Orch8r_admin_user():
        os.system('kubectl --namespace orc8r exec deploy/orc8r-orchestrator -- \
        /var/opt/magma/bin/accessc \
        add-existing -admin -cert /var/opt/magma/certs/admin_operator.pem \
        admin_operator')
        print("\n Create Orchestrator admin user \n")      

      def verify_admin_user_creation():
        os.system('kubectl --namespace orc8r exec deploy/orc8r-orchestrator -- /var/opt/magma/bin/accessc list-certs')
        print("\n Verify admin user creation\n")    

      def Remove_local_cert():
        os.system('rm -rf ~/secrets')
        print("\n Remove local certificates\n")   

    def display_DNS():
       print("After a few minutes, the NS records should propagate. Confirm successful deployment by visiting the host NMS organization at: https://host.nms.yoursubdomain.yourdomain.com Log in with the ADMIN_USER_EMAIL and ADMIN_USER_PASSWORD provided above.")
         
    def orch8r_access_API():
       def access_API():
          os.system('ping https://api.pmn-dev.wavelabs.in/swagger/v1/ui/')
          if  "Unable to connect" in str(os.system('ping https://api.pmn-dev.wavelabs.in')):
            print('\033[91m Unable to Connect to API Server \033[0m')

 