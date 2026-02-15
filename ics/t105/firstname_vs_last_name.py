full_name = "Cristian Cohen"
index = full_name.index(" ")
first_name = full_name[:index]
last_name = full_name[index+1:]

if len(first_name)>len(last_name):
    print("First name is longer VS last name")

else:
    print("Last name is longer VS last name")



