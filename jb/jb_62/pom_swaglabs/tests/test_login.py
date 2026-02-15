from playwright.sync_api import expect

from jb.jb_62.pom_swaglabs.pages.login_page import LoginPage


class TestLogin():


    def test_correct_login(self, setup_playwright):

        page = setup_playwright
        login_page = LoginPage(page)
        page.goto("https://www.saucedemo.com/")
        login_page.set_user_and_password()
        login_page.click_on_login()

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        assert page.url == "https://www.saucedemo.com/inventory.html","page URL is not as expected after login"



