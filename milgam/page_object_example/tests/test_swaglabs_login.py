from milgam.page_object_example.pages.product_page import ProductPage
from milgam.page_object_example.pages.welcome_page import WelcomePage


class TestSwaglabsLogin():

    def test_swaglabs_login_positive(self,setup_playwright_swaglabs):
        page = setup_playwright_swaglabs
        product_page = ProductPage(page)
        welcome_page = WelcomePage(page)

        welcome_page.login_by_user_password()
        welcome_page.get_error_message()


        print ("test end")