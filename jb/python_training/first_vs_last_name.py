first_name_length = 0
last_name_length = 0
full_name = "Matan_Regev"

# split to first and last name
# option1
for i in range(len(full_name)):
    if full_name[i] != "_":
        first_name = full_name[:i + 1]
    else:
        first_name_length = len(first_name)
        last_name_length = len(full_name) - first_name_length - 1
        break
#option 2
index = full_name.index("_")
first_name = full_name[:index]
last_name = full_name[index+1:]

# check for longest word
if first_name_length > last_name_length:
    print("first name length is longer VS last name length")
elif first_name_length == last_name_length:
    print("first name length is equals  last name length")
else:
    print("last name length is longer VS first name length")
