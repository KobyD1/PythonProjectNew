sum = 0

for i in range (0, 11):
    sum = i * 4
    print (sum)

    if (sum ==12):
        print ("the value is 12 ")
        continue
    if (sum>10):
        print ("the value is more than 10")
        # break - the loop is getting broken
        break
    print(f"temp is{sum}  ")

print ("Test end")