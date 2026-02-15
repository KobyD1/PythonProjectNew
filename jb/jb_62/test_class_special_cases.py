
class TestClassesExample():

    def test_swaglabs_correct_user_login_with_class(self, setup_playwright):
        print("into test_class_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        elements_with_spaces = page.query_selector_all(".input_error.form_input")  # example how to handle spaces in class
        
        elements_partial = page.query_selector_all("[class*=input_error]")
        print ("test end")