numbers = [343,2,6,0,232,4567,56]

length = len(numbers)
sum_by_loop = 0

for number in numbers:
    sum_by_loop += number

avg = sum(numbers) / length
avg_by_loop = sum_by_loop / length

print (avg)
