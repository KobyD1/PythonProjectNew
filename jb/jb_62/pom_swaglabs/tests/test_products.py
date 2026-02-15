from jb.jb_62.pom_swaglabs.pages.login_page import LoginPage
from jb.jb_62.pom_swaglabs.pages.product_page import ProductPage


class TestProducts:


    def test_verify_first_price_is_less_than_50 (self, setup_playwright):
        page = setup_playwright
        login_page = LoginPage(page)
        product_page = ProductPage(page)
        page.goto("https://www.saucedemo.com/")
        login_page.set_user_and_password()
        login_page.click_on_login()
        product_page.get_first_price()
