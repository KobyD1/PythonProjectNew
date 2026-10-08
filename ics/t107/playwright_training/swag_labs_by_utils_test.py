# import time
import time

from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()

page = utils.playwright_start("https://www.saucedemo.com/")

url = page.url

print (url)

user = page.locator("[id='user-name']")
user.fill("standard_user")
password = page.locator("[id='password']")
password.fill("secret_sauce")
login = page.get_by_text("Login")
login.click()
time.sleep(3)

prices = page.query_selector_all('[class="inventory_item_price"]')
# example how to go over all prices
for price in prices:
    price_text = price.inner_text()
    print (price_text)
l = len(prices)
print(f"the value of l is {l}")
# example how to get partial list
for i in range(3,5):
    price = prices [i]
    price_text = price.inner_text()
    print (f"the price by partial loop is {price_text}")

# example how to get spesific value from list
price =prices[4]
price_4 = price.inner_text()
print(f"the price by spesific  loop is {price_4}")

utils.playwright_stop()