import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
    first_name = page.locator("#input-firstname")
    first_name.fill("John")
    page.locator("#input-lastname").fill("Doe")
    page.get_by_placeholder("E-mail").fill("abc@aaaa.com")
    page.locator("[for='input-newsletter-yes']").click()
    time.sleep(1)
    page.locator("[class*='custom-control-label']").all()[2].click()
    page.get_by_text("Continue").click()





    browser.close()