num1 = 10
cntr = 100
i=3
is_dived = True
while (is_dived==True):
    # handling case of infinity by decreased countrt to 100

    i+=1

    result = num1%i
    if (result == 0):
        is_dived = False
        print(F"the result of deived in {i} is 0  ")
        continue

    cntr -= 1
    print(F"counter value is {cntr}")
    if (cntr == 0):
        break

