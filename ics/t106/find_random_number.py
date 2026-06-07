user_input  = input("Enter a number between 0 and 20:")
user_input_as_int = int(user_input)


if user_input_as_int>20 or  user_input_as_int<0:
    print (f"not allowed ,the number is  {user_input_as_int}")

else :

    num = 0

    while (not num == user_input_as_int):
        print (f"mismatch found the value is {num}")
        num = num+1
        # num+=1   example for add 1
        if num ==21:
            break
    print (f"getting out from loop ,the user define value  = {num}")
