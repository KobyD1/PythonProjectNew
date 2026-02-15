
def multiple(num1 , num2):
  print("multiple 2 numbers ",num1,num2)
  return num1 * num2
# anonimic lambda
multiple_by_lambda = lambda  x : x*2     # create function by lamda function 

fib=[0,1]
value=10
sum=fib[0]+fib[1]
for x in range (2,value):
    sum=fib[x-1] + fib [x-2]
    fib.append(sum)
    mult= multiple(fib[x-1],fib[x-2])
    print('value from mult is ',mult)
    
l= multiple_by_lambda(4)
print ('using function by kamda, l=',l)    







