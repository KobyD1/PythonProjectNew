nums =[23,-34,7,5,-12,34,-33,44,55,12]
# nums =[23,-34,7,-5]


summery_pos,summery_neg,summery_even,summery_odd = 0,0,0,0

for num in nums:
    if (num >0 ):
        print (f"{num} value is more than 0")
        summery_pos = summery_pos+num

    else:
        print (f"{num} value is less than 0")
        summery_neg = summery_neg+num

for num in nums:
    if (num %2 ==0 ):
        summery_even = summery_even+ num

    else:
        summery_odd = summery_odd + num



print ("Test End")

