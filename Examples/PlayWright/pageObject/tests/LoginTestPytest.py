import time
from turtle import position
from unittest import TestCase

from playwright.sync_api import Playwright, sync_playwright

from Examples.PlayWright.pageObject.pages.LoginPage import LoginPage


class TryTesting(TestCase):

    def test_ebay_pom_no_fixture(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("http://www.ebay.com")
            print(page.title())
            search = page.locator('#gh-ac')
            page.locator ('#gh-ac')

            search.dblclick()
            search.type("Phone2")
            cart = page.locator('svg.gh-cart-icon')
            cart.hover()
            assert page.title() == "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
            print('Test end')
            browser.close()

    def test_login(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False,args=["--start-maximised"])
            # p.chromium.launch({args: ['--start-maximized']});
            context = browser.new_context(no_viewport=True)
            # create a new page in a pristine context.
            page = context.new_page()
            page.goto("https://www.saucedemo.com/")
            login = LoginPage(page)
            login.login("standard_user","secret_sauce")
            page.close()


    def test_max(self):
        p = sync_playwright().start()
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        page.goto('https://www.google.com')

        time.sleep(3)


    def test_click(self):
        p = sync_playwright().start()
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        page.goto('https://www.ebay.com')
        page.get_by_text("Ship to").click(position={"x": 0, "y": 0})