from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://demo.guru99.com/test/newtours/register.php")
country_menu = driver.find_element(By.NAME,"country")
country_as_drop_down = Select(country_menu)
country_as_drop_down.select_by_index(3)
country_as_drop_down.select_by_visible_text("ANGOLA")



base.selenium_end()