#1.  given price as "38$" find the total price with tax of 2 $
# 2. given the following "the price of the shirt is 34$"
# find the product

price = "38$"
price = price.replace("$","")
total = "38$" + "2$"
price_as_int = int(price)
total= price_as_int+2
total_final = F"{total}$"
print (total_final)
