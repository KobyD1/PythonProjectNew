import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("[id='user-name']")
    user_name.click()
    user_name.clear()
    user_name.fill("standard_user")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_button = page.locator("[name='login-button']")
    login_button.click()
    time.sleep(2)
    prices  = page.locator("[class='inventory_item_price']").all()
    price_first = prices[0]
    price_text = price_first.inner_text()
    print(price_first)

    for price in prices:
        price_text = price.inner_text()
        print(price_text)

        price_text_ils = price_text.replace("$","ILS")


    url = page.url




    browser.close()