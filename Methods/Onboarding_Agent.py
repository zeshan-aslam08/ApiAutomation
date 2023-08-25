import requests
import json
import jsonpath
from Logs import loggers
from test_data.test_data import payload, invalid_payload, invalid_Name_payload, franchise_payload

########################***Agent Login***#################################
class LoginPage:
    log = loggers.log_fun()

    # Method with Valid Credentials
    def login_with_valid_credentials(self):
        """
        This Login API is used for valid credentials
        :return: status
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
        except Exception as e:
            self.log.error(f"An error occurred during the request: {e}")
            flag = False
        return flag

    #
    # Method with in Valid Credentials
    def login_with_invalid_credentials(self):
        """
        This Login API is used for valid credentials
        :return: status
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
        :return: status
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

#########################***Forget Password***#########################
    def Create_Franchise_with_valid_credentials(self):
        """
        Create a franchise with a valid credentials Method
        :return:status
        """
        flag = True
        response = requests.post("https://dev-corporate.mytmdev.com/api/create-franchise", data=franchise_payload)
        response_status = response.status_code
        print(response_status)
        if response_status != 200:
            flag = False
        else:
            print(f"f(Response Code :{response_status}")
        return flag

