import json

data_as_string = '{"ID":"1237777"     ,"Name": "John"}'

data_as_json = json.loads(data_as_string)     # from str to json
print (data_as_json["Name"])
data_as_string_from_json = json.dumps(data_as_json)  # from json to str

print ("Test End")

