from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseSelenium(object):

    def __init__(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = driver

    def selenium_init(self, url):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        sleep(3)
        return driver

    def selenium_end(self):
        self.driver.close()
