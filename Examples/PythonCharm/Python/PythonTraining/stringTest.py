test_string = "GFG"
  
add_string = " is best"
  
print("The original string : " + str(test_string)) 
  
# printing original add string  
print("The add string : " + str(add_string)) 

final1="".join((test_string, add_string)) # join 
print("after add:",final1) 
before_join = ['a','b','c','d','e']  # join over list 
print (''.join(before_join))

txt = "aabcdef"
txt.strip()     #trim
exist1 = txt.count('a')
exist2 = txt.count('ab')
exist3 = txt.count('eeree')
x = txt.replace("b", "bctttttt")
txt_nums = '1122'
txt_nums_1 = 'a1122'
txt_nums_1.isdecimal()   #check if it is nums only
txt.isdigit()
print(x)
