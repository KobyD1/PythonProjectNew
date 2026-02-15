summery = 0
count = 0
for i in range(1, 11):
    summery = summery + i
    count += 1

avg = summery / count
print(avg)

nums = [23, 45, 234, 565, 67, 66, 1, 1, 1, 3]
summery_list = 0
for num in nums:
    summery_list = summery_list + num

amount = len(nums)
avg_list = summery_list / amount
print(avg_list)
