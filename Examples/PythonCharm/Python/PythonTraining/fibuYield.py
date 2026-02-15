# yield - the function continue to run after the return , must include while to stop it

def fibo(n):

   num1, num2 = 0, 1
   cntr = 0
   while cntr < n:
       yield num1

       tmp = num1 + num2
       num1 = num2
       num2 = tmp
       cntr += 1


fib_object = fibo(10)
print(list(fib_object))