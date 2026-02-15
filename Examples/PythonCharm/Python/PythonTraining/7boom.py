import random

low_limit=0
high_limit=20
ref=7
r = random.randint(1, 10)

for x in range (low_limit,high_limit):
    if (x-ref==0):
        print ('num  found , num=',x)
    if ('7' in str(x)):
        print('num contains found , num=',x)



