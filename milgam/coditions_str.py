text = "Hi , My name is John i leave Rome"
city = "Lod"
city_5 = "Haifa"
num_3 = 9
num_as_str = "qwqwqw111121"

# int_casting = int(num_as_str)

boolean_example = False

# check if string contains Rome
if ("Rome" in text):
    print("John Leave in Rome")

if (city == "Lod"):
    print(f"city is {city}")

if (not boolean_example):
    print("print in case of Boolean ")

# check if value is only digits
if ( num_as_str.isdigit()):
    int_casting  = int (num_as_str)
    print (num_as_str)
