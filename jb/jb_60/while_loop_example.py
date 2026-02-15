
is_pass= False
counter = 0

# example of while in case of False (by not)
while not (is_pass):
    print ("The value of is pass is True")
    print (counter)
    counter+=1 # example of adding value
    if (counter==5):
        is_pass =True
        continue
    if (counter>10):
        break