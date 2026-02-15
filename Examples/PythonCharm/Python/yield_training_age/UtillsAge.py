import math
from datetime import date

today = date.today()

results = {
           '10': 0,
           '20': 0,
           '30': 0,
           '40': 0,
           '50': 0,
           '60': 0,
           '70': 0,
           '80': 0,
           '90': 0
           }



def age_parser(age_row):
    index = age_row.rindex("/")
    row_year = int(age_row[index + 1:index + 5])
    current_year = int(today.year)
    age = current_year - row_year
    return age


def flu_parser(age_row):
    if "Yes" in age_row:
        return True
    if "No" in age_row:
        return False


def age_counter(age, is_flu):
    if is_flu:
        results_group = str(math.floor(age / 10) * 10)
        result_value = results.get(results_group) + 1
        results[results_group] = result_value
    return results

def results_parser():
    print('######## Results ########')
    # for x in total.keys():
    #     print ('Total flu for age ',x + " => " + str(Results[x]))

