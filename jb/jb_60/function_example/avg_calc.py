
num1 = 12
num2 = 24

nums = [23,55,66,1000,77,88,77]

summery = num1+num2
avg = summery/2
print (avg)


summery_by_list = 0
for num in nums:
    summery_by_list = summery+num

len= len(nums)

avg_by_list = summery_by_list/len
print (avg_by_list)