

# go over all numbers from 0 to 20
# in the first time we get num that dived by 7
# print the number and stop the loop

# init variables
is_pass = True
counter = 0
# set while loop VS is_pass
while(is_pass):
    print (counter)
    counter+=1
    # checking if number at counter dived by 7
    if (counter%7 ==0):
        is_pass =False
 # adding defend for case of infinity loop , it will stop in 20 in any case
    if (counter==20):
        print("we got max value loop stoped ")
        break

print ("resolved by for loop ")
for i in range (1,20):
    print (f" the value of i is {i}")
    if (i % 7 ==0):

        break