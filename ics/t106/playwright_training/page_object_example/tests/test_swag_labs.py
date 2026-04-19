from ics.t106.playwright_training.page_object_example.pages.page_product import PageProduct
from ics.t106.playwright_training.page_object_example.pages.page_welcome import PageWelcome


def test_login_correct_details(setup_playwright_swaglabs):
    page = setup_playwright_swaglabs
    page.goto("https://www.saucedemo.com/")
    page_welcome = PageWelcome(page)
    page_product=PageProduct(page)
    page_welcome.set_login()
    print ("test end")



def test_login_correct_details(setup_playwright_swaglabs):
    page = setup_playwright_swaglabs
    page.goto("https://www.saucedemo.com/")
    page_welcome = PageWelcome(page)
    page_product=PageProduct(page)
    page_welcome.set_login()
    page_product.get_prices()
    print ("test end")