import json
import requests
from Examples.PythonCharm.Python.api.globals import *



def test_response_code():
    print("into response code test")
    response =requests.get(base_url+'pet/1245')
    response_code = response.status_code
    user_response = response.json()
    id = user_response["id"]
    name = user_response["name"]
    assert response_code == 200 ,"response code is not 200 as expected"
    assert (id,name) == (1245,"xyz"),"One or more response elements is not as expected "


def test_post():

   response = requests.post(base_url+'user',headers=headers, data=json.dumps(user))
   response_code = response.status_code
   response_user = response.json()
   message = response_user["message"]
   assert response_code == 200