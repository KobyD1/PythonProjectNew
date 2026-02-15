from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class BaseSelenium(object):
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.driver = driver




    def selenium_init(self,url):

        driver=self.driver
        driver.get(url)
        driver.maximize_window()
        sleep(3)
        return driver

    def test_end(self):
        self.driver.close()
        print ("Test End")




