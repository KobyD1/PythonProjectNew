

full_name  = "Leo Messi"
l= len(full_name)
index_1 = full_name.index("M")
index_2 = full_name.index(" ")
first_name = full_name[0:index_2]  # slicing
last_name = full_name[index_2+1:l]
first_name_v1 = full_name[:index_2]

full_name_strip=full_name.strip()
full_name_lower = full_name.lower()
full_name_after_replace = full_name.replace("Leo", "Leonid")
full_name_upper = full_name.upper()
split = full_name.split(" ")

full_name_upper = full_name.upper()


print (f"the length of {full_name} is {l}")
