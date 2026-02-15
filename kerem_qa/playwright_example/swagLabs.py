from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    user = page.locator("[id='user-name']")
    password = page.locator("[id='password']")
    user.fill("standard_user")
    password.fill("secret_sauce")
    login = page.locator("[id='login-button']")
    login.click()

    expect (page).not_to_have_url("https://www.saucedemo.com/")


    prices = page.query_selector_all('[class="inventory_item_price"]')
    for price in prices:
        print (price.text_content())
        print (price.inner_text())
    browser.close()