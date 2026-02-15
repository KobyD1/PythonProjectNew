from selenium.common import WebDriverException
from selenium.webdriver import Keys

from noTraffic.Pages.Locators import WelcomePageLocators


class WelcomeNTPage(object):


    def __init__(self, driver):
        self.driver = driver


# method for clicking on get all zones btn
    def click_on_get_all(self):
        get_all = self.driver.find_element(*WelcomePageLocators.WELCOME_BUTTONS)
        get_all.click()

# method for clicking on create zone btn
    def click_on_create_zone(self):
        self.click_on_get_all()
        create = self.driver.find_elements(*WelcomePageLocators.WELCOME_BUTTONS)[1]
        create.click()

    # method for analyze if create zone is clickable

    def create_zone_is_clickable(self):
        self.click_on_get_all()
        create = self.driver.find_elements(*WelcomePageLocators.WELCOME_BUTTONS)[1]
        try:
            create.click()
            return True
        except WebDriverException:
            return False

