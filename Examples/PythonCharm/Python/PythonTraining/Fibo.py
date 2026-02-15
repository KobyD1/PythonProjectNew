# 1,1,2,3,5,8,


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


fib_test = []
count = 100

if count <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence is ")
    for i in range(count):
        result = recur_fibo(i)

        fib_test.append(result)


print (fib_test)
print('## end of recursive print ##')
