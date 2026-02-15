import csv

with open("university_records_v1.csv", 'r', newline='') as file:
    csv_reader = csv.reader(file)

    # Method 1a: Print all rows as lists
    print("--- Reading All Rows ---")
    for row in csv_reader:
        print(row)
        print (row[1])