from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    search = page.locator('[id="gh-ac"]')
    search.click()
    search.clear()
    search.fill("Phone")
    search_button = page.locator('[id="gh-search-btn"]')
    search_button.click()
    print ("test end")

    browser.close()