from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    search = page.locator('#gh-ac')
    search.click()
    search.clear()
    search.fill("Phone")
    assert page.title() == "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"

browser.close()