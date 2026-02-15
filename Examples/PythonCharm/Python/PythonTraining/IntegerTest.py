maxNum=19
result=[]

for base in range (maxNum):       # scan all numbers up to maxNum
    for num in range (2,base):    # scan all numbers in range from 2 tobase
        if (base%num==0):
            break
        else:
            if (num==base-1):
                result.append(base)

print(result)

for base1 in range (1,10,2):     # scan all numbers from 1 to 10 with step 2
    print ('the value of base1 is',base1)

maxNum = 15
for base in range (maxNum):       # scan all numbers up to maxNum
        if (base==10):
            break

        if (base == 5):
            continue
        else:
            print (base)


print(result)


#mainContent > div.s-answer-region.s-answer-region-center-top > div > div.clearfix.srp-controls__row-2