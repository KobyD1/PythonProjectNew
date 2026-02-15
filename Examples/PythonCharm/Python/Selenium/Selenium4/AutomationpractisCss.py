import math

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class AutomationpractisLink(BaseSeleniumCommon):
    base=BaseSelenium()
    driver= base.selenium_init("https://www.saucedemo.com/")
    base.login_to_swagLabs("standard_user","secret_sauce")
     # "http://automationpractice.com/index.php?id_category=3&amp;controller=category"
    prices = driver.find_elements(By.CSS_SELECTOR,"div.inventory_item_description > div.pricebar > div[class='inventory_item_price']")
    add_charts = driver.find_element(By.CLASS_NAME('inventory_item_name'))
    total = 0
    for price in prices:
        value = price.text
        value = value.replace('$','')
        value.isdigit()
        value.isdecimal()

        value_as_float = float(value)
        total=total+value_as_float

    avarage = total/len(prices)
    math.ceil(avarage)
    print("the avarage value is "+str(math.ceil(avarage)))
    base.test_end()