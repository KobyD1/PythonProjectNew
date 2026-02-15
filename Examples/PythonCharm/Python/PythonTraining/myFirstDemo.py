first_name = 'Koby'
last_name = 'Davidof'
age= 1964

# printing my details
print ("My name is",first_name,last_name)
print ("I born in ",age)
if (first_name=='Koby'):
    print ('found')
if (age==1964):
    print ('num found')

if (first_name.count('K',0,6)):
    print ('include found')



if (first_name.__contains__('Ko')):
    print ('include found contains')

if ('Ko' in first_name):
    print ('in is working')
