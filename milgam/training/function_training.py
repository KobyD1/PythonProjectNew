# given 3 names
# each name define according "Avi Cohen",
# for each name
#     make sure it contains " "
#     split to first name and last name
#     print the results
# return according last name first name
from milgam.training.split_by_sign import full_name


def check_names(text):
    print(f" the value is {text}")
    full_name = ""
    if " " in text:
        splitted = text.split(" ")
        full_name = splitted[1]+ splitted[0]

    else:
        print ("space did not found into tested name")

    return full_name


name_1 = "Olga Yair"
name_2 = "Dan Cohen"
name_3 ="Avi Levi"
name_4 = "Olga_yairError"
full_names = []

full_name_1 = check_names(name_1)
full_name_2 =check_names(name_2)
full_name_3 =check_names(name_3)
full_name_4 =check_names(name_4)

full_names.append(full_name_1)
full_names.append(full_name_2)
full_names.append(full_name_3)
full_names.append(full_name_4)
print ("end ")



