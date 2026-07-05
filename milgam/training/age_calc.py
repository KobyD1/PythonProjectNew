# 0-18 – child
# 19-60 – adult
# 61-120 – senior

def calc_age(input_age):

    if input_age < 19 and input_age > 0:
        print (f"child found {input_age}")

    elif input_age >= 19 and input_age <=60:
        print (f"Adult found the vslue is {input_age}")

    elif input_age > 60 and input_age <= 120:
        print (f"Senior found {input_age}")

    else:
        print (f"not defined age found the value is {input_age}")

    return 25





ages =[5,8,67,45,0,120]

age_my_child =9
result = calc_age(age_my_child)

for age in ages:

    calc_age(age)


