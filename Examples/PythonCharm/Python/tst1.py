def multiple(num1,num2):
    print ('try to find multiple of ',num1," ",num2)
    return num1*num2

class tst1 :
    name='abcde'
    numbers = [1, 2, 3, 4, 5, 6]
    print (name[1:3])

    for x in range (0,10):
        if (x==5):
            print ('x equal 5')
        else:
            print (x)

    numbers.insert(3,7)
    l=len(numbers)
    for number in numbers:
        print (number)

    multiple(numbers[1],numbers[4])