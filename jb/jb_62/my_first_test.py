# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("#user-name")
    user.fill("standard_user")
    password = page.locator("#password")
    password.fill("secret_sauce")
    login_btn = page.get_by_text("login")
    login_btn.click()
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/inventory.html" ,"current URL is not as expected"
    page.close()
    browser.close()
    print ("Test end****")