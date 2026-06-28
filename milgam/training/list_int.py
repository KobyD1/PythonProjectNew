grades = [45,88,34,66,78,77]
sum = 0
cntr = 0
for grade in grades:
    sum = sum+grade
    a= grades[7]*2
    cntr +=1
    avg_temp = sum/cntr
    print (avg_temp)
avg_as_float = sum/len(grades)

avg = int(sum/len(grades))
avg = sum//len(grades)

avg = round(avg,0)
print (avg)

