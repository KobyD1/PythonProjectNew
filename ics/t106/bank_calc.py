balance= 1000
print ("please define transfer by user")
user_input = input()
user_input_as_int = int(user_input)
print (user_input)
final = balance+ user_input_as_int

if final > 0 :
    print (f"allowed ,the final balance is {balance}")

else:
    print (f" not allowed ")


