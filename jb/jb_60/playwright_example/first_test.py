from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")

    search = page.locator("[id='gh-ac']")
    search.click()
    search.clear()
    search.fill("Phone")
    search_button = page.locator("[id='gh-search-btn']")
    search_button.click()
    # page.keyboard.press('Enter')
    current_url = page.url
    assert page.url.__contains__("ebay"),"page URL did not contains Ebay after search"


    browser.close()
    print ("Test End")