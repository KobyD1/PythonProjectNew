def calc_multiple (num1, num2,num3=1):
    print(F"calculating num1 multiple by num2 ")
    if num1 > 0 and num2 > 0:
        result = num1 * num2 *num3
    print(F"the value of  num1 multiple by num2 is {result} ")

    return result

var1 = 4
var2 = 5
# main part
calc_multiple(var1,var2,8)
result = calc_multiple(56,67)
result_1= result+4