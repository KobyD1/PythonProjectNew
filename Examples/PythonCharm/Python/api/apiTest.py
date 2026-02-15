import json

import requests

url_base = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type':'application/json'}
user = {
    "id": 3333,
    "username": "user1",
    "firstName": "John",
    "lastName": "David",
    "email": "abc@gmail.com",
    "password": "123456",
    "phone": "054123456",
    "userStatus": 0
}


def test_get_status_code():
    response =requests.get(url_base+'pet/1245')
    assert  response.status_code == 200
    json = response.json()
    print ("Test End")


def test_get_body():
    response =requests.get('https://petstore.swagger.io/v2/pet/1245')
    json_as_dict = response.json()    # get data from the response as dictionary
    id = json_as_dict ['id']   # getting specific field
    category = json_as_dict['category']  # getting object as dictionary from response
    name = json_as_dict['category']['name'] # getting field from object as dictionary
    assert name =='xyz'
    assert id == 1245

def test_get_response_list():
    response = requests.get(url_base+'pet/findByStatus?status=pending')
    json_pets = response.json()
    l = len(json_pets)
    assert len(json_pets) > 0 , 'Pets not found as a response to pending '
    for pet in range (0,l):
        id = json_pets[pet]['id']
        name = json_pets[pet]['name']
        tags = json_pets[pet]['tags']    # find list per each pet
        len(tags)
        # assert len(tags) > 0 , 'tags not found as a body to tested pet '

        print ('\n'+' pet found ,id='+str(id)+',name ='+name)

def test_post():

   response = requests.post(url_base+'user',headers=headers, data=json.dumps(user))
   response_code = response.status_code
   assert response_code == 200

def test_post_v():
   url = "http://mock-api-env.eba-7vxf99wf.us-east-1.elasticbeanstalk.com/v1/login"
   user = {
  "username": "vectorious@medtech.com",
 "password": "Aa123456"


 }
   response = requests.post(url,headers=headers, data=json.dumps(user))
   response_code = response.status_code
   assert response_code == 200
def test_post_update():

   response = requests.post(url_base+'user',headers=headers, data=json.dumps(user))
   response_code = response.status_code
   assert response_code == 200
   code_from_res_body = response.json()["code"]
   # the body at response is
   # {
#     "code": 200,
#     "type": "unknown",
#     "message": "6874986831"
# }
   assert code_from_res_body == 200