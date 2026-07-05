# getting prices and calculate price per each price


def tax_calc(price_to_calc,tax_value):
    price_to_calc = price_to_calc.replace("$","")
    price_as_int = int(price_to_calc)
    tax = price_as_int * tax_value/100

    return tax


tax_from_user = 25
total = 0
prices = ["5$","23$","4$","30$"]
for price in prices:
    tax = tax_calc(price,tax_from_user)
    total += tax
    print (f"tax found {tax}")
print (f"total found {total}")




