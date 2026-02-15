import pytest
from playwright.sync_api import sync_playwright, expect

from qa09.swaglabs_pom.pages.login_page import loginPage
from qa09.swaglabs_pom.pages.product_page import productPage



@pytest.fixture()
def setup_swaglabs():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        login_page = loginPage(page)
        product_page = productPage(page)

        yield page,login_page,product_page
        print("### Test end ###")
        page.close()
        browser.close()
