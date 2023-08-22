import requests
import json
import jsonpath

from test_data.test_data import payload


class loginPage:


    def login_with_valid_cridentials(self):
        flag = True
        response = requests.post("https://dev-corporate.mytmdev.com/api/sale-agent-signin", data=payload)
        response_status = response.status_code
        print(response_status)
        if response_status == 200:
            flag = True
        return flag
