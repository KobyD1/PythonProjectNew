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
        product_page = ProductPage(page)
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password("failure","secret_sauce")
        is_visible = welcome_page.get_error_message()
        assert is_visible == True , "Login did not success as expected"
        print ("test end")