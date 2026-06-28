city = "London"
l = len(city)
counter_o = city.count("o")
counter_f = city.count("f")
city_2_prefix = "Petach-"
city_2_suffix = "Tikva"
index = city.index("n")
city = city.replace("L","l")
full_city = city_2_prefix+city_2_suffix
is_city_digit = city.isdigit()
num_as_str = "12.3"
is_num_digit = num_as_str.isdigit()

full_name = "Avraham.cohen Izhak.Levi Yaacov.Ben.Izhak"
full_name_split_2 = full_name.split(".")
full_name_splited = full_name.split(" ")
second_father = full_name_splited[1]
second_father_splitted = second_father.split(".")
second_father_last = second_father_splitted[1]
is_digit = second_father.isdigit()
print ("test end")
