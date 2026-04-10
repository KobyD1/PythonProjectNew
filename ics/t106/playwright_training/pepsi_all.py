# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.pepsi.com/")
    buttons = page.query_selector_all(".nav-link-text")
    for button in buttons:
        print (button.inner_text())


    page.close()
    browser.close()
    print ("Test end****")