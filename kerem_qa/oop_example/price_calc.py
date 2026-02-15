
def price_calc(price):
    if 0<price < 100:
        print ("Price is between 0 to 100")

    elif 100<price<1000:
        price = price+20
        print (F"Price is between 100 to 1000, new price is {price}")

    elif price>1000:
        price = price + 50
        print(F"Price is more than 1000, new price is {price}")


    else:
        print("invalid Price")
    return price


# main part
price_calc(-50)
price_new = price_calc(50)
print(price_new)
if price_new%2==0:
    print ("Dived by 2 number found ")
else:
    print ("Dived by 2 number not found ")

    price_new = price_calc(100)
    print(price_new)
price_calc(101)
price_calc(1005)


