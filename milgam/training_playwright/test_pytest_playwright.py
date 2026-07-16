

class TestPytestPlaywright():

    def test_swaglabs_start(self,setup_playwright):
        page =setup_playwright
        page.goto("https://www.saucedemo.com/")
        print ("test end")

    def test_swaglabs_login(self,setup_playwright):
        page =setup_playwright
        page.goto("https://www.saucedemo.com/")
        user_name = page.locator("[id='user-name']")
        user_name.click()
        user_name.clear()
        user_name.fill("standard_user")
        password = page.locator("[id='password']")
        password.fill("secret_sauce")
        login_button = page.locator("[name='login-button']")
        login_button.click()
        print ("test end")


