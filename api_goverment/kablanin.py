import csv

import requests

url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=4eb61bd6-18cf-4e7c-9f9c-e166dfa0a2d8&limit=100&filters={"SHEM_YISHUV":["חולון          "]}'

response = requests.get(url)
data = response.json()

data_excel_all  = []
data_excel  = {}



field_names = ['EMAIL', 'MISPAR_KABLAN', 'MISPAR_TEL', 'SHEM_YESHUT','SHEM_YISHUV']





if data['success']:
    records = data['result']['records']
    l = len(records)
    for record in records:
        row = {
            'EMAIL': record.get('EMAIL', ''),
            'MISPAR_KABLAN': record.get('MISPAR_KABLAN', ''),
            'MISPAR_TEL': record.get('MISPAR_TEL', ''),
            'SHEM_YESHUT': record.get('SHEM_YESHUT', ''),
            'SHEM_YISHUV': record.get('SHEM_YISHUV', '')
        }
        print(f" num constructor is : {row['MISPAR_KABLAN']}")
        print(f" city is  : {row['SHEM_YISHUV']}")


        data_excel_all.append(row)

with open('kablanim_records_v1.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data_excel_all)