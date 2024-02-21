# import required packages from package.py module
import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
sys.path.append(root_dir)
from backend.configs.package import *

logging.captureWarnings(True)
root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
execution_date = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
log_file_path = root_dir + "\\reports\logs\\"
# create directory with the current date and time
os.makedirs(log_file_path+f"{execution_date}", exist_ok=True)
# Open log file with current execution date
file_name = os.path.basename(__file__)
log_file_path = log_file_path + f"{execution_date}\\" + f"{file_name}-{execution_date}.txt"
log_file = open(log_file_path, 'w')
dir_path = root_dir + "\\backend\configs"
with open(f'{dir_path}/configs.yaml', 'r') as file:
    values = yaml.safe_load(file)
with open(f'{dir_path}/user-config.yaml', 'r') as file:
    user_values = yaml.safe_load(file)


class Post_Subscriber(unittest.TestCase):

    def setup(self):
        # Define all variables in setup function --to be done
        self.url = values['url']
        self.cert = values['cert']
        self.key = values['key']

    def test_post_subscriber(self):
        print("\nStarting Post APN test:\n")
        log_file.write("\nStarting Post APN test\n")
        cert_path = root_dir + values['cert']
        key_path = root_dir + values['key']
        json_path = root_dir + values['json_add_subscriber']
        network_subscriber = user_values['network_subscriber']
        subscriber_name = user_values['subscriber_name']
        subscriber_id = user_values['subscriber_id']
        with open(f'{json_path}', 'r') as f:
            json_data_obj = json.load(f)
        rPost = requests.post(url=(values['url'] + f"lte/{network_subscriber}/subscribers"), cert=(cert_path, key_path), json=json_data_obj, verify=False)
        print(str(rPost.text))
        log_file.write(str(rPost.text))
        if rPost.status_code == 201:
            print("\nPost Subscriber Test passed. The response code is:\n")
            print(str(rPost.status_code))
            log_file.write("\nPost Subscriber Test passed. The response code is:\n")
            log_file.write(str(rPost.status_code))
            self.assertEqual(rPost.status_code, 201)
        else:
            print("Post Subscriber Test failed. The response code  is:\n")
            log_file.write("Post Subscriber Test failed. The response code is:\n")
            print(str(rPost.status_code))
            log_file.write(str(rPost.status_code))
            self.assertEqual(rPost.status_code, 201)

        # verify the added subscriber is present using get command
        print("\n\nVerifying added Subscriber is present:\n")
        log_file.write("\n\nVerifying added Subscriber is present:\n")
        time.sleep(5)
        rGet = requests.get(url=(values['url'] + f"lte/{network_subscriber}/subscribers/{subscriber_id}"), cert=(cert_path, key_path), verify=False)
        if rGet.status_code == 200:
            print(f"\nSubscriber {subscriber_name} is added as expected. \n")
            log_file.write(f"\nSubscriber {subscriber_name} is added as expected. \n")
            self.assertEqual(rGet.status_code, 200)
        else:
            print(f"\nSubscriber {subscriber_name} is not added. \n ")
            log_file.write(f"\nSubscriber {subscriber_name}is not added. \n ")
            self.assertEqual(rGet.status_code, 200)

    def tearDown(self):

        time.sleep(5)
        print("\nPost subscriber Test ended\n")
        log_file.write("\nPost subscriber Test ended\n")
        print(f"\nReport stored at:\n{log_file_path}\n")
        log_file.close()


if __name__ == "__main__":
    unittest.main()
