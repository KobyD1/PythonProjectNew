nums = [23,12,11,22,3,5,6,-23,9,10]
odd_summery = 0
even_summery = 0

for num in nums:
    if num % 2 == 0:
        print ("Even num found the value is"+" { "+f"{num} ")
        even_summery+=num

    else:
        print (f"Odd num found the value is {num} ")
        odd_summery+=num
    num = num + 1
    print ("loop end")

    print (f"odd summery is {odd_summery} , even summery is {even_summery}")

