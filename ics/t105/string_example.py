
full_name = 'Koby Cohen'
full_name_as_upper = full_name.upper()
print (full_name_as_upper)
length = len(full_name)
index = full_name.index(" ")
first_name = full_name[0:index]
last_name = full_name[index+1:length]
first_name_v1 = full_name[:index]
last_name_v1 = full_name[index:]
price = " 22228$"
price=price.replace("$"," ILS")
count =price.count("287")
price_no_space = price.strip()

# casting example
num1 = 21
num2= 1
counter = num1+num2
counter_as_str = str(counter)   # convert from int to string

num_as_str = "75545"
num_as_int= int(num_as_str)      # convert from string to integer




print ("test end")