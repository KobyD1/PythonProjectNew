# 1,1,2,3,5,8,


fibo_res = [0,1]

count = 100

for i in range (2, count):
    num = fibo_res[i-1]+fibo_res[i-2]
    fibo_res.append(num)

print(fibo_res)