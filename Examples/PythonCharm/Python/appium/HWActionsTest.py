import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


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

    def test_calculate_tap(self) :
        print('into test')
        # Find calculator digit buttons
        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_2')
        digit1 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_1')
        
        # Create TouchAction object for hardware actions
        actions = TouchAction(self.driver)
        actions.tap(digit2)
        actions.tap(digit1)
        actions.perform()
        
        time.sleep(2)
        print('test stop')



