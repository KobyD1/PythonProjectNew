import csv

data = [{'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
        {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1}
    , {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3}
    , {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5}
    , {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8}
    , {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}]

data[2]["year"]=1900


field_names = ['name', 'branch', 'year', 'cgpa']


with open('university_records_v1.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

with open("university_records_v1.csv", mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # Method 1a: Print all rows as lists
    print("--- Reading All Rows ---")
    for row in csv_reader:
        print(row)
        print (row[1])
