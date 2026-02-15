
from playwright.sync_api import sync_playwright


class TestPlaywright():
    def test_assert_only_pass(self):
        assert 1 == 1

    def test_assert_only_pass_1(self):
        assert 1 == 1

    def test_playwright(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.saucedemo.com/")
            user = page.locator("[id='user-name']")
            password = page.locator("[id='password']")
            login_button = page.get_by_text("Login")
            login_button_by_name = page.locator("[name='login-button']")  # example for name
            user.fill("standard_user")
            password.fill("secret_sauce")
            login_button.click()
            assert page.url == "https://www.saucedemo.com/inventory.html", "URL after login is not as expected "

            page.close()
            browser.close()
            print("### Test end ###")
