"""
Title: Bevo test Script
Author: Micky Kumar
Created Date: 2024-01-26
Updated Date: 2024-01-26
"""
import pytest
import datetime
import os
import logging
import subprocess

@pytest.fixture
def log_file_path():
    logging.captureWarnings(True)
    execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    os.makedirs(f"{execution_date}", exist_ok=True)
    # Open log file with the current execution date
    file_name = os.path.basename(__file__)
    log_file_path = f"{execution_date}\\" + f"Automation-{file_name}-{execution_date}.txt"
    
   # with open(log_file_path, 'a') as log_file:
        #log_file.write(f"{execution_date}: This is the setup method")

    return log_file_path

class TestBevo:
    def test_setup_method(self, log_file_path):
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"\n{datetime.datetime.now()}: Setting up method...")
            #configuration

    def test_upgrade_bevo(self, log_file_path):
        def upgrade_package():
            # Run the 'apt update' command
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"\n{datetime.datetime.now()}: Start apt update")
            # subprocess.run(["sudo", "apt", "update"])
            command = "sudo apt upgrate"

            # Run the command and capture the output
            subprocess.run(command, shell=True, capture_output=True, text=True)

        def test_upgrade_branch():
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"\n{datetime.datetime.now()}: - Start upgrade branch")
            command1 = "git checkout development"
            command2 = "git status"
            command3 = "git pull origin development"

            # Run the command and capture the output
            subprocess.run(command1, shell=True, capture_output=True, text=True)
            subprocess.run(command2, shell=True, capture_output=True, text=True)      
            subprocess.run(command3, shell=True, capture_output=True, text=True)
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"\n{datetime.datetime.now()}: - complete upgrade branch")        

        # Call the upgrade_package function
        upgrade_package()
        test_upgrade_branch()

    def test_upgrade_orch8r(self, log_file_path):
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"\n{datetime.datetime.now()}: - Upgrading Orch8r...")
            log_file.write(f"\n{datetime.datetime.now()}: - Complete Upgrading Orch8r...")

    def test_add_subscriber(self, log_file_path):
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"\n{datetime.datetime.now()}: Adding subscriber...")
            command = " go run main.go add -subscriber_id 001011234567537 -auth_key 5E4AB35891375d2AEE812E67C309A629 -auth_opc A3782F73B17811F4043EE66EBFD62519  -lte_auth_next_seq 13761 -lte_subscription_active true"
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                log_file.write(f"\n{datetime.datetime.now()}: Command executed successfully!")
                print(f"Output: {result.stdout}")
            else:
                log_file.write(f"\n{datetime.datetime.now()}: Command failed! \nError: {result.stderr}")


    def test_teardown(self, log_file_path):
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"\n{datetime.datetime.now()}: Tearing down...")

# Example usage
if __name__ == "__main__":
    # Create an instance of TestBevo
    test_bevo_instance = TestBevo()

    # Call the setup log function to get the log_file
    log_file_variable = test_bevo_instance.log_file_path

    # Use the log_file in the setup method
    test_bevo_instance.test_setup_method(log_file_variable)

    # Use the log_file in the other methods
    test_bevo_instance.test_upgrade_bevo(log_file_variable)
    test_bevo_instance.test_upgrade_orch8r(log_file_variable)
    test_bevo_instance.test_add_subscriber()

    # Use the log_file in the teardown method
    test_bevo_instance.test_teardown()
