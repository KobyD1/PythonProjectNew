from jb.jb_60.function_example.utils import utils

utils_instance=utils()


price_1 = "27$"
price_2 = "33$"
price_3 = "44$"
price_4 = 40.0
rate= 3.4
new_price_1 = utils_instance.getting_vat(price_1)
new_price_2 = utils_instance.getting_vat(price_2)
utils_instance.add_suffix(new_price_1,rate)
utils_instance.add_suffix(new_price_2,rate)
utils_instance.add_suffix(price_4,4.1)

print ("Test End")


# find VAT (18%) per each price
# convert it to ILS

