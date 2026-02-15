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


response = requests.post(url_base+'user',headers=headers, data=json.dumps(user))
print (response.status_code)
