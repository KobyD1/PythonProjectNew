import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("[id='user-name']")
    password=page.locator("[id='password']")
    password = page.locator("[id='password']")
    login_button =page.locator("[id='login-button']")
    user_name.fill("standard_user")
    password.fill("secret_sauce")
    login_button.click()

    time.sleep(2)