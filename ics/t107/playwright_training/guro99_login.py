import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/index.php")

    user_name = page.locator("[name='userName']")
    password =page.locator("[name='password']")
    submit = page.locator("[name='submit']")
    user_name.fill("tutorial")
    password.fill("tutorial")
    submit.click()

    time.sleep(1)