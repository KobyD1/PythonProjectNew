price_1 = "26$"
price_2 = '30$'

price_1_as_text = price_1.replace("$", "")
price_2_as_text = price_2.replace("$", "")
price_1_as_int = int(price_1_as_text)
price_2_as_int = int(price_2_as_text)

if (price_1_as_int > price_2_as_int):
    print("price 1 is bigger VS price 2")

elif (price_1_as_int < price_2_as_int):
    print("price 2 is bigger VS price 1")

else:
    print("Both of prices are equals")

print("Test End")
