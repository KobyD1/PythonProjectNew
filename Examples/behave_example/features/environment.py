from selenium import webdriver

def before_all(context):
    print ("Before all tests")

    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    context.num1 = 10

def after_all(context):
    context.driver.quit()

