import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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
        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_2')
        digit1 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_1')

        actions = TouchAction(self.driver)
        actions.tap(digit2)
        actions.tap(digit1)
        actions.perform()

        actions.tap(digit1)
        actions.long_press(digit2)
        actions.double_tap(digit2)
        actions.perform()

        actions.move_to(digit2,100.50)  # swipe right / up




        print('test stop')

    def test_swipe(self):
        print('into swipe test')
        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.android.calculator2:id/digit_2')

        actions = TouchAction(self.driver)
        actions.move_to(digit2,100.50)
        actions.perform()
        print ('test stop')
        digit1 = self.driver.find_element(By.ID, 'com.android.calculator2:id/digit_1')


        print('test stop')

