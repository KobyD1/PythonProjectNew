import json

from aqua.globals import value_to_find, json_file


def test_get_query_source():
    f = open(json_file)
    data = json.load(f)
    rows_counter= len(data)
    live_in_query_counter = 0
    for row in data:
        for key, value in row.items():
            if value.get('querySource') == value_to_find:
                live_in_query_counter += 1

    f.close()
    print (f"{live_in_query_counter} with query to {value_to_find} found of total {rows_counter} rows ")
    print ("test end")
