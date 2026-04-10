# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    buttons = page.get_by_role("link",name="Calculator").all()
    button =page.get_by_role("link", name="Calculator").nth(8)
    button.click()
    buttons_by_text = page.get_by_text("Calculator").all()
    button_by_text = page.get_by_text("Calculator").nth(10)
    button_by_text.click()


    page.close()
    browser.close()
    print ("Test end****")