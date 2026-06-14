full_name = 'Moni_Richard'
# given full name
# to split it to first and last name
index = full_name.index("_")
first_name= full_name[0:index]
length= len(full_name)
last_name= full_name[:index+1]
last_name= full_name[index+1:]

last_name= full_name[index+1:length]
print (f"the values are : {last_name}  , {first_name}")
print ("test end")
