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
        assert "$7.99" == text






