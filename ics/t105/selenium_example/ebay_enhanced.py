# from t105.selenium_example.selenium_base_105 import seleniumBase105
from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()
driver.get('https://www.ebay.com/')

base.selenium_end()
