from behave import given, when, then


@given("I am on the SauceDemo login page")
def step_impl(context):
    print ("I am on the SauceDemo login page")
    # context.num1 = 10
    print (F"*******{context.num1}")
    # context.page = LoginPage(context.driver)
    # context.page.load()

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    print ("I am on the SauceDemo login page")
    # context.page.login(username, password)

@when('Login failed')
def step_impl(context):
    print ("I am on the SauceDemo login page")

@then("I should be redirected to the products page")
def step_impl(context):
    assert 1 ==1
    print ("I should be redirected to the products page")