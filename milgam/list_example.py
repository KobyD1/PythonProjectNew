first_names = ["Michal","David","John",'dan']
name_first = first_names[1]
name_before_last = first_names[-2]
name_1 = "Yehudit"
name_1 = name_1.lower()  # how to oconver to lower case
name_1 = name_1.capitalize()

name = first_names[1].lower()
l = len(first_names)
first_names.append("Moshe")  # add at the end of the list
first_names.insert(2,"Nehami")  # add at spesific place
first_names.remove("Michal")
index = first_names.index("John")
counter = first_names.count("John")    # count the number of spsific vale

name_first = first_names[1]   # getting from spesific place

if 'Dan' in first_names:   # check if list contains spesific value
    first_names.remove("Dan")

print ("Test end")
