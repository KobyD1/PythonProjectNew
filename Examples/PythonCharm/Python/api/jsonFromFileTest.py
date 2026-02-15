import json
import os


def test_get_file_as_object():

    f = open('Data/employees.json')      # Opening JSON file
    data = json.load(f)  # returns JSON object as
    for i in data['employee']:   # move over all data as list
        print(i)
        print (i['name'])

    f.close() # close the file

def test_create_file_as_json():

    developer = {
        "name":"Dev1",
        "grade":77,
        "city":"TLV"

    }

    # with open("Data/developer_file.json","w") as file:  # another option to open file
    file = open("Data/developer_file.json","w")

    json.dump(developer,file)
    file.close()
    is_exist = os.path.isfile("Data/developer_file.json")
    assert is_exist == True , 'File not found as expected'