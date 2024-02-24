import os
import sys

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.logging import *
from backend.configs.package import *



class TestGetpodsNRFStatus(unittest.TestCase):

    def test_setup_openvpn_connected(self):
        try:
            process = subprocess.Popen(["tasklist", "/fi", "imagename eq openvpn.exe"], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, universal_newlines=True)
            process_output, _ = process.communicate()

            self.assertTrue("openvpn.exe" in process_output.lower())


        except subprocess.CalledProcessError as e:
            self.fail("Error checking OpenVPN connection: {}".format(e))

    def setUp(self):
        bevo_url = values['bevo_url']
        bevo_user = values['bevo_user']
        bevo_pass = values['bevo_pass']
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(bevo_url, username=bevo_user, password=bevo_pass)


    def tearDown(self):
        self.ssh_client.close()
        log_file.write("\n\nClose the SSH connection\n")

    def test_get_nrf_status(self):
        ssh_command = 'ssh on-prem'
        stdin, stdout, stderr = self.ssh_client.exec_command(ssh_command)
        time.sleep(2)

        kubectl_command = 'kubectl get po -A -o wide |grep nrf'
        stdin, stdout, stderr = self.ssh_client.exec_command(kubectl_command)

        kubectl_output = stdout.read().decode('utf-8')
        print("kubectl output:")
        print(kubectl_output)
        log_file.write("\n\nkubectl output:\n")
        log_file.write(kubectl_output)

        exit_status = stdout.channel.recv_exit_status()
        print(exit_status)
        log_file.write("\n\nCheck the exit status of the kubectl command\n")

        if exit_status == 0:
            log_file.write("kubectl command succeeded\n")
        else:
            log_file.write("kubectl command failed\n")
            log_file.write("kubectl error output:\n")
            error_output = stderr.read().decode('utf-8')
            log_file.write(error_output)


        if exit_status != 0:
            print("kubectl command failed with exit status", exit_status)

        log_file.write("\n\nClose the SSH connection\n")


if __name__ == '__main__':
    unittest.main()
