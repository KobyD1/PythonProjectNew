import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    search_menu =page.locator('[id="gh-ac"]')
    search_menu.click()
    search_menu.clear()
    search_menu.fill("Shoes Zara ")

    search_button = page.get_by_role("button",name="Search")
    search_button.click()




    print ("test end")

    browser.close()