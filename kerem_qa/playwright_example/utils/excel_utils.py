import csv
import time


class excelUtils:


    def get_excel_row_data(self,row_number,file_name):
        data = []
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for col in reader:

                data.append(col[row_number])

        return data

    def set_excel_data(self,data,file_name):

        field_names = [ 'ID', 'Price']
        data_to_excel = [
            {field_names[0]: 'Price1', field_names[1]: data[0]},
            {field_names[0]: 'Price2', field_names[1]: data[1]},
            {field_names[0]: 'Price3', field_names[1]: data[2]},
            {field_names[0]: 'Price4', field_names[1]: data[3]},
            {field_names[0]: 'Price5', field_names[1]: data[4]},
            {field_names[0]: 'Price6', field_names[1]: data[5]}

                  ]

        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data_to_excel)
