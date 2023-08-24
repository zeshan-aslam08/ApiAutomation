import requests
import json
import jsonpath
from Logs import loggers
from test_data.test_data import payload, invalid_payload, invalid_Name_payload


class LoginPage:
    log = loggers.log_fun()

    # Method with Valid Credentials
    def login_with_valid_credentials(self):
        """
        This Login API is used for valid credentials
        :return: flag indicating success or failure
        """
        flag = True
        try:
            response = requests.post("https://dev-corporate.mytmdev.com/api/sale-agent-signin", data=payload)
            response_status = response.status_code
            self.log.info(f"Status Code is : {response_status}")

            if response_status != 200:
                self.log.info(f"Status Code is {response_status} not 200")
                flag = False
            else:
                self.log.info(f"Status Code is Correct {response_status}")
            # if not response.json()['Token']:
            #     self.log.info("Token does not exist in the response")
            #     flag = False
            # else:
            #     self.log.info("Token exists in the response")
        except requests.exceptions.RequestException as e:
            self.log.error(f"An error occurred during the request: {e}")
            flag = False
        return flag

    #
    # Method with in Valid Credentials
    def login_with_invalid_credentials(self):
        """
        This Login API is used for valid credentials
        :return: flag indicating success or failure
        """
        flag = True
        try:
            response = requests.post("https://dev-corporate.mytmdev.com/api/sale-agent-signin", data=invalid_payload)
            response_status = response.status_code
            self.log.info(f"Status Code is : {response_status}")

            if response_status != 200:
                self.log.info(f"Status Code is {response_status} not 200")
                flag = False
            else:
                self.log.info(f"Status Code is Correct {response_status}")
            # if not response.json()['Token']:
            #     self.log.info("Token does not exist in the response")
            #     flag = False
            # else:
            #     self.log.info("Token exists in the response")

        except requests.exceptions.RequestException as e:
            self.log.error(f"An error occurred during the request: {e}")
            flag = False
        return flag

    # Method with invalid Name
    def login_with_invalid_Name(self):
        """
        This Login API is used for valid credentials
        :return: flag indicating success or failure
        """
        flag = True
        try:
            response = requests.post("https://dev-corporate.mytmdev.com/api/sale-agent-signin",
                                     data=invalid_Name_payload)
            response_status = response.status_code
            self.log.info(f"Status Code is : {response_status}")

            if response_status != 200:
                self.log.info(f"Status Code is {response_status} not 200")
                flag = False
            else:
                self.log.info(f"Status Code is Correct {response_status}")
            # if not response.json()['Token']:
            #     self.log.info("Token does not exist in the response")
            #     flag = False
            # else:
            #     self.log.info("Token exists in the response")
        except requests.exceptions.RequestException as e:
            self.log.error(f"An error occurred during the request: {e}")
            flag = False
        return flag
