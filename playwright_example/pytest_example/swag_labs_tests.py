




class TestSwaglabs():
# def - saved word for function
# test - mandatory
    def test_login_correct_user(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        print("Trying to login with correct parameters ")
        user = page.locator("[id='user-name']")
        password = page.locator("[id='password']")
        login_button = page.get_by_text("Login")
        user.fill("standard_user")
        password.fill("secret_sauce")
        login_button.click()
        assert page.url =="https://www.saucedemo.com/inventory.html","URL is not as expectrd after login with correct user"


    def test_login_incorrect_user(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        print("Trying to login with incorrect parameters ")
        user = page.locator("[id='user-name']")
        password = page.locator("[id='password']")
        login_button = page.get_by_text("Login")
        user.fill("fake_user")
        password.fill("fake_password")
        login_button.click()
        print(f"URL found the value is{page.url} ")

        assert page.url == "https://www.saucedemo.com/","Page URL is not as expected after incorrect login"

    def test_get_first_price(self,setup_playwright):

        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        print("Trying to login with correct parameters ")
        user = page.locator("[id='user-name']")
        password = page.locator("[id='password']")
        login_button = page.get_by_text("Login")
        user.fill("standard_user")
        password.fill("secret_sauce")
        login_button.click()
        #analyze if login pass by login button
        is_login_fail=login_button.is_visible()
        assert is_login_fail==False, "Login button appears after login therefore login failed "
        prices = page.query_selector_all("[class='inventory_item_price']")

        for price in prices:
            price_as_str= price.text_content()
            print (price_as_str)
            price_as_str = price_as_str.replace("$","")
            price_as_float = float(price_as_str)
            is_pass = price_as_float<100 # getting results as boolean
            assert is_pass,"the Price is more than 100$"
        print("after quesry selector all")


    def test_login_by_css(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("input[id='user-name']")
        password = page.locator("input[data-test='password']")
        login_button = page.locator("input[class='submit-button btn_action']")
        user.fill("abc")
        password.fill("fake")
        login_button.click()
        print ("debug point")




