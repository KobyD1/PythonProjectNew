import json


jsonData = '{"ID":"123", "Name": "John"}'

data = json.loads(jsonData)   # loads - from string to json object
print (data['ID'])  # how to get any key

newData = {"DOB": "22-10-2001"}
data.update(newData)
print ('new key after update '+ data['DOB'])  # how to add new key

data_as_object = json.dumps(data)  # dumps - from json object to string
print(data)
len_string = len(data_as_object)  # return 51 as the length of the string
len_object = len(data)   # return 3 as the number of the keys
print('### Object### '+data_as_object)