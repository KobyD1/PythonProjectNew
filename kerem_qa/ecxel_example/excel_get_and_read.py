import csv
field_names = ["year", "avg_grade"]

file_name = 'grades.csv'
data = [
    {field_names[0]: 0, field_names[1]: 70},
    {field_names[0]: 0, field_names[1]: 90},
    {field_names[0]: 0, field_names[1]: 80},
    {field_names[0]: 0, field_names[1]: 80},
    {field_names[0]: 0, field_names[1]: 85 }

]

counter = 0

for year in range (2000,2005):
    data[counter][field_names[0]] = year
    counter =+1

with open(file_name, 'w', newline='') as file_to_write:
    writer = csv.DictWriter(file_to_write, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)


with open(file_name, 'r', newline='') as file_to_read:
    csv_reader = csv.reader(file_to_read)
    index = 0
    for row in csv_reader:
        if row[1] == '90':
            print (F"{row[1]} found in {index}")
            year = row[0]
            print (f"year: {year}")
        index =+1





print ("test end")