import csv



file_name = 'students_records_v2.csv'
field_names = ['Full Name', 'ID', 'Year', 'Salary']



data = [
    {field_names[0]: 'John Due', field_names[1]:0, field_names[2]: 1999, field_names[3]: 9000},
    {field_names[0]: 'Leo Messi', field_names[1]: 0, field_names[2]: 2001, field_names[3]: 9001},
    {field_names[0]: 'Luna Hasson', field_names[1]: 0, field_names[2]: 2005, field_names[3]: 8977},
    {field_names[0]: 'Lora Daxa', field_names[1]: 0, field_names[2]: 2012, field_names[3]: 9010},
    {field_names[0]: 'Maram Hasson', field_names[1]: 0, field_names[2]: 2001, field_names[3] :9000},
 
    
]

counter = 0
max_id = 1000 + len(data)
for i in range(1000,max_id):

    data[counter][field_names[1]]= i
    counter += 1


with open(file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)


names = []
with open("university_records_v1.csv",'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row) # getting data as row 
        # print(row[0]) # getting data from spesific col
        names.append(row[0])


print ("Test end")
