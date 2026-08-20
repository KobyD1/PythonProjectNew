price = "12$"


price_as_ils = price.replace("$", "ILS")

print (f"the value in ILS is {price_as_ils}")
price= price.replace("$","")
price_as_int = int(price)
final_price= price_as_int+3
print (f" the price aftyer tax is {final_price}")
#change it to ILS for example from 12$ to 12ILS
# add tax to price by adding 3$ for example the final price will be 15$
