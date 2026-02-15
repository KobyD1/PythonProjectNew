import time

from selenium.webdriver.common.by import By

from noTraffic.Pages.Locators import GetAllZonesPageLocetors, WelcomePageLocators
from noTraffic.Pages.WelcomeNTPage import WelcomeNTPage


class GetAllZonesPage(object):

    def __init__(self, driver):
        self.driver = driver
        welcomePage = WelcomeNTPage(driver)

    # method for clicking on delete_zone by line as argument, return the deleted zone
    def delete_zone_by_line(self, line):
        time.sleep(3)
        line = self.driver.find_elements(*GetAllZonesPageLocetors.LINE_CLICK)[line]
        line.click()
        pattern = line.text
        indx = pattern.find('\n')
        time.sleep(3)
        delete = self.driver.find_elements(By.CSS_SELECTOR, 'span.mat-button-wrapper')[2]
        delete.click()
        time.sleep(3)
        return pattern[:indx]

    # method for get zone text by line - line define as integer

    def get_zone_by_line(self, line):
        get_all = self.driver.find_element(*WelcomePageLocators.WELCOME_BUTTONS)
        get_all.click()
        lines = self.driver.find_elements(*GetAllZonesPageLocetors.LINE_TEXT)
        return lines[line].text

    # method to find the amount of  zones into table by name
    def get_zone_by_name(self, zone_name):
        get_all = self.driver.find_element(*WelcomePageLocators.WELCOME_BUTTONS)
        get_all.click()
        lines = self.driver.find_elements(*GetAllZonesPageLocetors.LINE_TEXT)
        cntr = 0
        for line in lines:
            if zone_name in line.text:
                cntr += 1

        return cntr

    # method to get all zone details per line - line define as string (zone name)
    def get_zone_all_details(self, zone_name):
        time.sleep(3)
        get_all = self.driver.find_element(*WelcomePageLocators.WELCOME_BUTTONS)
        get_all.click()
        lines = self.driver.find_elements(*GetAllZonesPageLocetors.LINE_TEXT)
        cntr = 0
        for line in lines:
            if zone_name in line.text:
                pattern = line.text
                break

        return pattern
