import pandas as pd
import numpy as np
import random

num_rows = 1000
data = []


for _ in range(num_rows):
    sys_temp = round(random.uniform(14.0, 85.0), 1)
    sys_pressure = round(random.uniform(1.0, 6.0), 1)
    milk_temp = round(random.uniform(3.0, 15.0), 1)
    water_qty = random.randint(10, 100)
    fill_tap = random.choice([0, 1])


    if sys_pressure > 3.0 and sys_pressure <4.5:
        cool_tap = random.choice([0, 1])

    if sys_pressure > 4.5 and sys_pressure < 6:
        cool_tap = 1
            #     if cool_tap == 0:
    #         defect = "Pressure_Failure"
    #         explanation = "תקלה! לחץ גבוה והברז סגור"
    #     else:
    #         defect = "None"
    #         explanation = "OK"
    # else:
    if milk_temp >= 10.0 or sys_temp >= 30.0:
        cool_tap = 1
        defect = "None"
        explanation = "OK"
    else:
        cool_tap = 0
        defect = "None"
        explanation = "OK"


    data.append([sys_temp, sys_pressure, milk_temp, water_qty, fill_tap, cool_tap, defect, explanation])

# יצירת ה-DataFrame
df = pd.DataFrame(data, columns=[
    'System Temp', 'System Pressure', 'Milk Temp', 'Water Quantity',
    'FillTap', 'CoolTap', 'CoolTap Defect', 'הסבר לסטודנט'
])

# שמירה לקובץ
df.to_csv('milk_system_data_ok_1000.csv', index=False, encoding='utf-8-sig')
print("file success to create")