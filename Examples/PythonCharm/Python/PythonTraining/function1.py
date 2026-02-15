def print_price(price):
    price_as_str = str(price)
    print('Price found = ' + price_as_str + 'NIS')

# second Function - calculate tax
def add_tax(price1, tax):
    final_price = price1 + price * tax
    return final_price

def return_list_example(price1, tax):
    result = []
    final_price = price1 + price * tax
    result.append(price)
    result.append(final_price)
    result.append(price)
    return result

# the code start here
price = 25
prefix = 'The price of the product is '
final = prefix + str(price) + '$'
print(final)

print_price(30)  # calling to first function

final_price = add_tax(price, 10) # calling to second function

print('Price changed to ' + str(final_price)) # using the result of second Func.
