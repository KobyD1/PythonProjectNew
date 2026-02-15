import time


class TestSwagLabsTest():

    def test_login(self,setup_playwright):
        print("test_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("[id='user-name']")
        user.fill("standard_user")

        password = page.locator("[id='password']")
        password.fill("secret_sauce")
        login_button = page.locator("[name='login-button']")
        login_button.click()
        time.sleep(3)
        url = page.url
        assert url == "https://www.saucedemo.com/inventory.html","Page URL is not as expected after login"

    def test_incorrect_login(self,setup_playwright):
        print("test_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("[id='user-name']")
        user.fill("standard_user")

        password = page.locator("[id='password']")
        password.fill("fake_secret_sauce")
        login_button = page.locator("[name='login-button']")
        login_button.click()
        url = page.url
        assert url == "https://www.saucedemo.com/","Page URL is not as expected after incorrect login"



