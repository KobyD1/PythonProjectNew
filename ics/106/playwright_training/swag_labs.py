# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    user.fill("standard_user")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_btn = page.get_by_text("log")
    login_btn.click()
    current_url = page.url
    print(current_url)
    page.close()
    browser.close()
    print ("Test end****")