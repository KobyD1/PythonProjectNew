import time
import unittest

from ics.t107.playwright_training.playwright_utils import PlaywrightUtils


class lastDayTest(unittest.TestCase):




    def test_manager_login(self):
        utils = PlaywrightUtils()

        page = utils.playwright_start("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        time.sleep(3)
        buttons = page.query_selector_all('[class="btn btn-primary btn-lg"]')
        button =buttons[1]
        button.click()

        utils.playwright_stop()

    def test_flight_checkbox(self):
        utils = PlaywrightUtils()
        page = utils.playwright_start("https://demo.guru99.com/test/newtours/reservation.php")
        trip_types = page.query_selector_all('[name="tripType"]')
        trip_type = trip_types[1]
        trip_type.click()

        utils.playwright_stop()

