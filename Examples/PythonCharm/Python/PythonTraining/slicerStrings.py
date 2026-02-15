# print sub string 
pattern = "May the Forces be with you."
print(pattern[2:10])
print(pattern[2:])  # print from place 2 to the end
print(pattern[:2])  # print from the begining to place 2
print(pattern[-3])  # print only single  letter ,  3 places from the string end
print(pattern[-3:-1]) # print sub string from -3 to -1 (2 letters)
index1=pattern.index('be')
index2=pattern.index('you')
print ('printing by index ,from index 1 to index 2 :', pattern [index1:index2])

# casting + combined strings 
string1='5'
x_int=int(string1)
print (x_int)
x_string=str(x_int)
x_string=x_string+'test5'
print('printing combined string :',x_string)
print('printing string twice :',x_string*2)  
dual_string=x_string*2
print(dual_string)

# add int to string 
print (x_string,x_int)   # add space between string to integer 
print (x_string+str(x_int))




