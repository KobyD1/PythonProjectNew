def avg_calc(num_to_calc_1, num_to_calc_2):
    print (f"Calc avg value between {num_to_calc_1} and {num_to_calc_2}")
    if num_to_calc_1 <0 : num_to_calc_1 = num_to_calc_1 * -1
    if num_to_calc_2 <0 : num_to_calc_2 = num_to_calc_2 * -1
    avg = (num_to_calc_1 + num_to_calc_2) / 2
    print (f"the avg value is {avg}")



num_1 = 10
num_2 = 20
num_3 = 30

avg_calc(num_1, num_2)
avg_calc(num_2, num_3)
avg_calc(num_1, num_3)


# if num_1 <0 : num_1 = num_1 * -1
# if num_2 <0 : num_2 = num_2 * -1
# avg= (num_1 + num_2 )/2
# print (f"the avg value is {avg}")
#
#
# if num_1 <0 : num_1 = num_1 * -1
# if num_3 <0 : num_2 = num_2 * -1
# avg= (num_1 + num_3 )/2
# print (f"the avg value is {avg}")
