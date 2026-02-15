# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    search_menu =page.locator("[id='gh-ac']")
    search_menu.click()
    search_menu.fill("Camera")
    page.keyboard.press("Enter")
    page.close()
    browser.close()
    print ("Test end****")