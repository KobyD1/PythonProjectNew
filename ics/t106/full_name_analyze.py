full_name = "Leonid Mess"
index = full_name.index(" ")
first_name= full_name[:index]
last_name = full_name[index+1:]
l_first_name= len(first_name)
l_last_name= len(last_name)
is_first_longer = l_first_name > l_last_name
if is_first_longer:
    print ("First name in longer than last name")
else:
    print ("Last  name in longer than first name")



print ("Test end")