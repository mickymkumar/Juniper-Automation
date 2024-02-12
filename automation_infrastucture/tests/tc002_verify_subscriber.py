"""
title: Create Subscriber
Updated Date: Feb 10, 2024
Author: Micky Kumar
"""
import subprocess
import logging
import datetime
import os

class VerifySubscriberTests:
    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)

    def test_kubectl_get_pods(self):
        # Execute the command: kubectl get pods -n pmn
        result = subprocess.run(["kubectl", "get", "pods", "-n", "pmn"], capture_output=True, text=True)
        
        # Check if the command executed successfully
        assert result.returncode == 0, f"Error: {result.stderr}"
        
        # Log the output
        self.log_output("kubectl_get_pods", result.stdout)

    def test_kubectl_exec_subscriber_cli(self, pod_name):
        # Execute the command: kubectl exec -it -n pmn "pod_name" -- subscriber_cli.py list
        result = subprocess.run(["kubectl", "exec", "-it", "-n", "pmn", pod_name, "--", "subscriber_cli.py", "list"],
                                capture_output=True, text=True)
        
        # Check if the command executed successfully
        assert result.returncode == 0, f"Error: {result.stderr}"
        
        # Log the output
        self.log_output("kubectl_exec_subscriber_cli", result.stdout)

    def log_output(self, command_name, output):
        # Create a logger
        logger = logging.getLogger(command_name)
        logger.setLevel(logging.DEBUG)
        
        # Create a file handler
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(self.log_dir, f"{command_name}-{current_date}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add the file handler to the logger
        logger.addHandler(file_handler)
        
        # Log the output
        logger.info(output)

# Example usage
if __name__ == "__main__":
    kubectl_tests = KubectlTests()
    kubectl_tests.test_kubectl_get_pods()
    # Provide the pod name for the second test
    kubectl_tests.test_kubectl_exec_subscriber_cli("pod_name")
