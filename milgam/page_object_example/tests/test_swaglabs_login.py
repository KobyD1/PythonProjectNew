import webbrowser

from milgam.page_object_example.pages.product_page import ProductPage
from milgam.page_object_example.pages.welcome_page import WelcomePage


class TestSwaglabsLogin():

    def test_swaglabs_login_positive(self,setup_playwright_swaglabs):
        page = setup_playwright_swaglabs
        product_page = ProductPage(page)
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password("standard_user","secret_sauce")
        assert page.url == "https://www.saucedemo.com/inventory.html" , "Login did not success as expecrted"

        print ("test end")


    def test_swaglabs_login_negative(self,setup_playwright_swaglabs):
        page = setup_playwright_swaglabs
        product_page = ProductPage(page)
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password("failure","secret_sauce")
        assert page.url == "https://www.saucedemo.com/" , "Login did not success as expecrted"

        print ("test end")

    def test_swaglabs_login_error_message(self,setup_playwright_swaglabs):
        page = setup_playwright_swaglabs
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password("failure","secret_sauce")
        is_visible = welcome_page.get_error_message_visible()
        act_text = welcome_page.get_error_message_text()
        exp_text = "Epic sadface: Username and password do not match any user in this service"
        assert exp_text == act_text , "Error message is not as expected"
        assert is_visible ==True , "Error message did not apears in case of incorrect login"
        print ("test end")


    def test_swaglabs_product_page_title(self,setup_playwright_swaglabs):
        page = setup_playwright_swaglabs
        product_page = ProductPage(page)
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password("standard_user","secret_sauce")
        product_page.get_title()
        print ("test end")