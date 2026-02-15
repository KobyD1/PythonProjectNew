from selenium.webdriver.common.by import By

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start_with_url("https://www.ebay.com")
search_menu = driver.find_element(By.ID,"gh-ac")
search_menu.click()
search_menu.send_keys("Shirt")
search_button = driver.find_element(By.ID,"gh-search-btn")
search_button.click()
price_all = driver.find_element(By.CLASS_NAME,"su-card-container__attributes.su-card-container__attributes--has-secondary")
print (price_all.text)
price_all_text = price_all.text

if ("delivery" in price_all_text):
    index_1 = price_all.text.index("+ILS")+4
    index_2 = price_all.text.index("delivery")
    delivery_price = price_all.text[index_1:index_2]
    delivery_price=delivery_price.strip()
    delivery_price=delivery_price.replace(".","#")
    print (delivery_price)

if ("shipping" in price_all_text):
    index_1 = price_all.text.index("+ILS")+4
    index_2 = price_all.text.index("shipping")
    delivery_price = price_all.text[index_1:index_2]
    delivery_price=delivery_price.strip()
    print (delivery_price)






base.selenium_stop()