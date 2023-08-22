import requests
import json

BaseUrl = "https://reqres.in/"


def test_get_request():
    response = requests.get(BaseUrl + "api/users?page=2")
    response_json = response.json()
    status_code = response.status_code
    print(status_code)
    # print(f"Response Body: {json.dump(response.content , indent= 4)}")
    print(response_json)

    if status_code == "200":
        print(f"Response Status Code:{status_code}")
    else :
        print(f"Error Occur: {status_code}")
    #  


