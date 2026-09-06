numbers = [343,2,6,0,232,4567,56]

size = len(numbers)
sum_by_loop = 0

for number in numbers:
    sum_by_loop += number

avg = sum(numbers)/size
avg_by_loop =sum_by_loop/size

print (avg)
