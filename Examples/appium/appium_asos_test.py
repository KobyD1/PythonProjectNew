import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_server_url_local = 'http://localhost:4723/wd/hub'
capabilities  = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appPackage='com.asos.app',
    newCommandTimeout= 120,
    appActivity='com.asos.mvp.view.ui.activity.reconsent.FullscreenReconsentPopUpActivity',
    language='en',
    locale='US'
)


class firstTestAppium(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Remote(appium_server_url_local, capabilities)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test1(self):
        skip = self.driver.find_element(by=AppiumBy.ID, value='//android.widget.TextView[@text="Continue with this app"]')

        skip.click()
        # search = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="Search here"]')
        # search.click()
        time.sleep(10)
        # time_before = time_element.text
        print(f'\n  time found ')






