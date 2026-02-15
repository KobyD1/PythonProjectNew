numbers = [3,5,6,7,6,66,78]
cities = ["London", "Athen","New-York","Jerusalem","Lod" ]

l = len(numbers) # find the length of list
value = numbers[2] # geting the value at index 2
index_of_5 = numbers.index(5)  # getting the position of 5 in list
numbers.append(56)
numbers.insert(2,77)
counter = numbers.count(6)


for number in numbers:
    print (number)
    if (number < 10):
        print(f" {number} found - it less than 10")
        number+=10
        print(f" {number} is the new number")


    if (number%2 ==0):
        print (f"{number} dived by 2")
