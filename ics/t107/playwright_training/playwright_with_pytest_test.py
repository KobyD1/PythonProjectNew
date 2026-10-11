import time
import unittest

from ics.t107.playwright_training.playwright_utils import PlaywrightUtils


class examplePlaywrightTest(unittest.TestCase):




    def test_swag_lab_price(self):
        utils = PlaywrightUtils()

        page = utils.playwright_start("https://www.saucedemo.com/")

        url = page.url

        print(url)

        user = page.locator("[id='user-name']")
        user.fill("standard_user")
        password = page.locator("[id='password']")
        password.fill("secret_sauce")
        login = page.get_by_text("Login")
        login.click()
        time.sleep(3)

        prices = page.query_selector_all('[class="inventory_item_price"]')

        text = prices[4].inner_text()
        assert text =="$7.99"
        assert "$" in text
        assert text.count("$") == 1
        utils.playwright_stop()



    def test_swag_lab_price_0(self):
        utils = PlaywrightUtils()

        page = utils.playwright_start("https://www.saucedemo.com/")

        url = page.url

        print(url)

        user = page.locator("[id='user-name']")
        user.fill("standard_user")
        password = page.locator("[id='password']")
        password.fill("secret_sauce")
        login = page.get_by_text("Login")
        login.click()
        time.sleep(3)

        prices = page.query_selector_all('[class="inventory_item_price"]')

        text = prices[0].inner_text()
        assert text =="$29.99"
        utils.playwright_stop()


    def test_swag_lab_prices(self):
        utils = PlaywrightUtils()

        page = utils.playwright_start("https://www.saucedemo.com/")

        url = page.url

        print(url)

        user = page.locator("[id='user-name']")
        user.fill("standard_user")
        password = page.locator("[id='password']")
        password.fill("secret_sauce")
        login = page.get_by_text("Login")
        login.click()
        time.sleep(3)

        prices = page.query_selector_all('[class="inventory_item_price"]')
        for price in prices:
            text = price.inner_text()
            print (text)
            assert "$" in text

    def test_swag_lab_login(self):
        utils = PlaywrightUtils()



