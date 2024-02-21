import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *

logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\logs\\"
os.makedirs(log_file_path + f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
console = sys.stdout
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Put_Gateway(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']
        self.json_data = values['json_data']

    def test_put_gateway(self):
        print("\nStarting Put LTE Gateway test:\n")
        log_file.write("\nStarting Put LTE Gateway test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_put_gateway']
        network_gateway = user_values['network_gateway']
        gateway_id = user_values['get_gateway_id']
        with open(f'{json_path}', 'r') as f:
            json_data_obj = json.load(f)
        print ("Editing Gateway description, dhcp server, ip_block")
        rPut = requests.put(url=(values['url'] + f"lte/{network_gateway}/gateways/{gateway_id}"), cert=(cert_path, key_path), json=json_data_obj, verify=False)
        print(rPut.text)
        log_file.write(rPut.text)
        if rPut.status_code == 204:
            print("\nPut LTE Gateway Test passed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write("\nPut LTE Gateway Test passed. The response code is:\n")
            log_file.write(str(rPut.status_code))
            self.assertEqual(rPut.status_code, 204)
        else:
            print("Put LTE Gateway Test failed. The response code  is:\n")
            log_file.write("Put LTE Gateway Test failed. The response code is:\n")
            print(str(rPut.status_code))
            log_file.write(str(rPut.status_code))
            self.assertEqual(rPut.status_code, 204)

        # verify the edited Gateway using get command
        print("\n\nVerifying edited LTE Gateway using GET command:\n")
        log_file.write("\n\nVerifying edited LTE Gateway using GET command:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/{network_gateway}/gateways/{gateway_id}"), cert=(cert_path, key_path), verify=False)
        if rGet.status_code == 200:

            print(f"\nLTE Gateway {gateway_id} is edited as expected. \n")
            log_file.write(f"\nLTE Gateway {gateway_id} is edited as expected. \n")
            print(rGet.text)
            log_file.write(rGet.text)
            self.assertEqual(rGet.status_code, 200)
        else:
            print(f"\nLTE Gateway {gateway_id} is not edited. \n ")
            log_file.write(f"\nLTE Gateway {gateway_id}is not edited. \n ")
            self.assertEqual(rGet.status_code, 200)

    def tearDown(self):

        time.sleep(5)
        print("\nPut LTE Gateway Test ended\n")
        log_file.write("\nPut LTE Gateway Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
