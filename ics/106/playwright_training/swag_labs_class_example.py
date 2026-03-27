from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user =page.locator('[name="user-name"]')
    password = page.locator('[name="password"]')
    login_button = page.get_by_text("Login")

    user.click()
    user.fill("standard_user")
    password.click()
    password.type("secret_sauce")

    login_button.click()
    url = page.url
    print (url)

    prices = page.query_selector_all('[class="inventory_item_price"]')
    first_price = prices[0]
    print (first_price.inner_text())

    for price in prices:
        text = price.inner_text()
        text=text.replace("$","")
        print(f"price found the value is {text}")
        text_as_float = float(text)

        if text_as_float >25:
            print (f"High price found, the price is {text_as_float}")


    print ("test end")
    browser.close()