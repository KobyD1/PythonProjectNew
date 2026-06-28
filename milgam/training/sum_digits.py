def digits_summery_by_str(num_to_analyze):
    if len(num_to_analyze) == 3:
        print(f"{num_to_analyze} is correct")
        sum=0
        for digit in num_to_analyze:
            digit_as_int = int(digit)
            sum += digit_as_int
        return sum

    else:
        print(f"{num_to_analyze} is incorrect")
        return

def digits_summery_by_int  (num_to_analyze):
    if num_to_analyze>99 and num_to_analyze<1000:
        print(f"{num_to_analyze} is correct")
        last_digit = num_to_analyze%10
        second_digit = num_to_analyze%100//10
        first_digit = num_to_analyze//100
        summery = last_digit + second_digit + first_digit
    else:
        print(f"{num_to_analyze} is not correct")

    return summery


number ="123"
number_as_int = 234
sum = digits_summery_by_str(number)
digits_summery_by_str("1234")
sum_as_int = digits_summery_by_int(number_as_int)