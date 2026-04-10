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

    drop_down_sort = page.locator("[class='product_sort_container']")
    # drop_down_sort.select_option(index=2)
    drop_down_sort.select_option("Price (low to high)")

    print ("test end")
    browser.close()