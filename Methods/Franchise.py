import requests

from test_data.test_data import franchise_payload


#########################***Create Franchise***#########################
class CreateFranchise:

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


#################################***Franchise TopUp***#################################















#################################***Franchise TopUp List***#################################
