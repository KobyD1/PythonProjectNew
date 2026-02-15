import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    deviceName='Pixel 3 XL API27',
    appPackage='com.android.calculator2',
    appActivity='com.android.calculator2.Calculator',
    language='en',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723/wd/hub'

class TestAppium(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.driver.implicitly_wait(30)
    def tearDown(self) :
        if self.driver:
            self.driver.quit()

    def test_calculate_click(self) :
        print('into test')
        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_2')
        digit1 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_1')
        digit1.click()
        digit2.click()
        time.sleep(3)


        print('test stop')

