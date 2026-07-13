import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.starbucks.com/")
    # order_buttons = page.get_by_text("Order now").all()
    order_button = page.get_by_text("Order now")
    order_button.click()





    browser.close()