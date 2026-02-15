prices = ["28$","32$","16$","20$"]
# for each price replace $ in ILS
#     for each price add 2 to the price

for price in prices :
    price = price.replace("$","ILS")
    print (f"the new price is {price}")
    price_only_digits=price.replace("ILS","")
    price_as_int = int(price_only_digits)
    price_as_int=price_as_int+2
    price=(f"{price_as_int}+ILS")







