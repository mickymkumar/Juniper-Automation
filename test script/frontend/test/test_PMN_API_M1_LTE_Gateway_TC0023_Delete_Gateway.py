import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *

logging.captureWarnings(True)
# Get root directory of the project
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
# Open log file with execution date
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + f"\\reports\logs\\"
os.makedirs(log_file_path + f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"


log_file = open(log_file_path, 'w')
# Open config files
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Delete_Gateway(unittest.TestCase):
    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_delete_gateway(self):
        print("\nStarting Delete LTE Gateway test...\n\n")
        log_file.write("\nStarting Delete LTE Gateway test...\n\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        network_gateway = user_values['network_gateway']
        gateway_id = user_values['delete_gateway_id']
        print(f"LTE gateway id to Delete:{gateway_id}\n")
        log_file.write(f"LTE gateway id to Delete:{gateway_id}\n")
        # Send Delete request
        rDelete = requests.delete(url=(values['url'] + f"lte/{network_gateway}/gateways/{gateway_id}"), cert=(cert_path, key_path), verify=False)
        print("\nResponse body:\n" + str(rDelete.text))
        log_file.write("\nResponse body:\n" + str(rDelete.text))

        if rDelete.status_code == 204:
            print("\nDelete LTE Gateway Test passed. The Response code is: ")
            print(str(rDelete.status_code))
            log_file.write("\nDelete LTE Gateway Test passed. The Response code is: ")
            log_file.write(str(rDelete.status_code))
            self.assertEqual(rDelete.status_code, 204)
        else:
            print("Delete LTE Gateway Test failed. The Response code is not 204 (OK) and it is: ")
            log_file.write("Delete LTE Gateway Test failed. The Response code is not 204 (OK) and it is: ")
            print(str(rDelete.status_code))
            log_file.write(str(rDelete.status_code))
            self.assertEqual(rDelete.status_code, 204)

        print("\n\nVerifying deleted LTE gateway is not present:\n")
        log_file.write("\n\nVerifying deleted LTE gateway is not present:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/{network_gateway}/gateways/{gateway_id}"),
                            cert=(cert_path, key_path),
                            verify=False)

        if rGet.status_code != 200:
            print(f"\nLTE gateway {gateway_id} is deleted as expected\n")
            log_file.write(f"\nLTE gateway {gateway_id} is deleted as expected\n")
            self.assertNotEqual(rGet.status_code, 200)

        else:
            print(f"\nLTE gateway {gateway_id} is not deleted and is still present\n ")
            log_file.write(f"\nAPN {gateway_id} is not deleted and is still present\n ")
            self.assertNotEqual(rGet.status_code, 200)

    def tearDown(self):
        time.sleep(5)
        print("\n\nDelete LTE Gateway Test ended\n")
        log_file.write("\n\nDelete LTE Gateway Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
