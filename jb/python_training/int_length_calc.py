from jb.python_training.utils import Utils_jb61

nums = [123,241,34,234,678,234,12]

# go over all list memebers
# in case the number is 3 digits (by function)- find the summery of all digits
# e.g :
# 123 ->6
# 34-> printing any error mewssage
# the activity will be by function

utils = Utils_jb61()
for num in nums:
    sum = utils.find_digits_summery(num)
    print (f"the value is {sum}")
