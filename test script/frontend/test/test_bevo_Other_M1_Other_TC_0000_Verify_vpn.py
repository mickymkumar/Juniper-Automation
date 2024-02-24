import unittest
import subprocess

class TestOpenVPNConnection(unittest.TestCase):

    def test_openvpn_connected(self):
        try:
            # Run the 'tasklist' command to list running processes and pipe the output to 'findstr' to search for OpenVPN
            process = subprocess.Popen(["tasklist", "/fi", "imagename eq openvpn.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            process_output, _ = process.communicate()

            # Check if the process_output contains "openvpn.exe" indicating that OpenVPN is running
            self.assertTrue("openvpn.exe" in process_output.lower())

            # Optionally, you can add additional checks to ensure the OpenVPN process is connected.
            # For example, you can search for specific configuration file names or log entries.

        except subprocess.CalledProcessError as e:
            # If the 'tasklist' or 'findstr' command fails, consider the connection as not established
            self.fail("Error checking OpenVPN connection: {}".format(e))

if __name__ == '__main__':
    unittest.main()
