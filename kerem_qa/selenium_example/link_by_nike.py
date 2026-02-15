from selenium.webdriver.common.by import By

from kerem_qa.playwright_example.utils.playwright_utils import PlaywrightUtils
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
# driver = base.selenium_start()
#
# driver.get("https://www.nike.com/il/")
driver = base.selenium_start_with_url("https://www.nike.com/il/")
utils = PlaywrightUtils()

woman_text =driver.find_element(By.LINK_TEXT,"Women").text
driver.find_element(By.PARTIAL_LINK_TEXT, "Find").click()

url = driver.current_url
print(url)

if (url == 'https://www.nike.com/il/retail'):
    print("Test OK - URL as expected")

else:
    print("#####Test FAILED - URL not as expected######")

base.selenium_stop()
