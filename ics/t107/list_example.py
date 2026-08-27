numbers = [11,23,33,65,163,5,398,11]
results = []
numbers.append(42)         # example how to add a number to the list
length = len(numbers)      # how to find the length of the list
index = numbers.index(23)
counter = numbers.count(11)
num_temp = numbers[3]

for number in numbers:
    print(number)
    if number > 10:
        print ("Number is greater than 10")

    else:
        print ("Number is less than 10")
    result = number * 10
    results.append(result)
    print(f"the result is {result}")

print ("test end")
