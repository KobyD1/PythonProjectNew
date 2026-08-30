# find the summery of positive numbers
# and the summery of the negative numbers
# at 2 diffrent variables

nums = [1,4,6,-4,-10,3,0,-5,7,9]
positive_sum = 0
negative_sum = 0

for num in nums:
    if num == 0:
        break
    elif num > 0:
        positive_sum = positive_sum + num

    else:
        negative_sum = negative_sum + num

print (f"negative  sum {negative_sum}")
print (f"positive sum {positive_sum}")
