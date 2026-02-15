from behave import given, when, then


@given("init calculator")
def step_impl(context):
    print ("I am in given")

@when("set first number")
def step_impl(context):
    print ("I am in when")
    num1 =3

@when("set second number")
def step_impl(context):
    print ("I am in when2")
    num2 =4

@when("set third number")
def step_impl(context):
    print ("I am in when3")
    num3 =-5

@then("get the numbers summery results")
def step_impl(context):
    print ("I am in then")


@then("get the numbers multiple results")
def step_impl(context):
    print ("I am in multiple numbers")