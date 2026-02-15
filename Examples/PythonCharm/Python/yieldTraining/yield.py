# A simple generator function
def my_gen(num):
    n = num
    print('This is printed first1 n=',n)
    # Generator function contains yieldTraining statements
    yield n

    n += 1
    print('This is printed second2 n=',n)
    yield n

    n += 3
    n +- 1
    print('This is printed at last3 n=',n)
    yield n

a = my_gen(20)

next(a)
next(a)
next(a)
# restart the counter by create another instant of the generator
b=my_gen(30)
next(b)
