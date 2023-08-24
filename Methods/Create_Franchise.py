import requests

from test_data.Franchise_data import payload


class CreateFranchise:

    def Create_Franchise_with_valid_credentials(self):
        flag = True
        response = requests.post("https://dev-corporate.mytmdev.com/api/create-franchise", data=payload)
        response_status = response.status_code
        print(response_status)
        if response_status != 200:
            flag = False
        else:
            print(f"f(Response Code :{response_status}")
        return flag
