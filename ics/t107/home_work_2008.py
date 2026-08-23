full_name ="Alona Due"
index = full_name.index(" ")
first_name = full_name[0:index]
first_name_short = full_name[:index].strip()  # another example for slicing

l = len(full_name)
last_name =full_name[index+1:8]
last_name_1 = full_name[index+1:l]   # example how to gwt by length
last_name_2 = full_name[index+1:] # another example how to find by default value
last_name_with_space = full_name[index:l]
last_name_strip_example = last_name_with_space.strip()  # example how to strip the string , remove spaces
# how to wrote it shortly
full_name ="Alona Due"
index = full_name.index(" ")
first_name_short = full_name[:index].strip()
last_name = full_name[index+1:].strip()
print (f"first name is {first_name_short},last name is {last_name}")
full_name_swap = last_name_1+" "+first_name

if len(last_name) > len(first_name_short):
    print ("The last name is longer than first name")
else:
    print ("The first name is longer than last name")



print ("test end")
