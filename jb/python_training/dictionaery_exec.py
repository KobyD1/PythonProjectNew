from jb.python_training.utils import Utils_jb61

# staring the code

user_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "abc@abc.com",
    "age": 42

}

user_2 = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "john@abccom",
    "age": 16

}

utils = Utils_jb61()
age_1 = Utils_jb61().age_calculator(user_1["age"])
age_2 = utils.age_calculator(user_2["age"],20)
is_valid = utils.email_validator("aaaa@dfdd.com")
is_valid = utils.email_validator("@.")

if is_valid:
    utils.send_mails()
print (f"{age_1} and  {age_2}")
