low_num = int(input("please define the low limit"))
high_num = int(input("please define the high limit"))

if low_num > high_num:
    temp = low_num
    low_num = high_num
    high_num = temp

for i in range(low_num,high_num+1):
    if ( i % 3 ==0):
        print(i)


print ("test end")