# 1. getting lists with ages analyse for each age if it is >65
# in case of >65 print senior found
# other print normal found
# [12,67,87,23,55]
# 2. create list with all numbers from 1 to 10

ages = [12,67,87,23,55]

for age in ages:
    print (f"analyze {age} years old")
    if age > 65:
        print("Senior found")
    else:
        print("Normal found")

