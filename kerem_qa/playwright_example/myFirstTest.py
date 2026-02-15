from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    expect(page).to_have_title("Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay")

    assert page.title()== r"Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
    search = page.locator('#gh-ac')
    search.click()
    search.clear()

    search.fill(" Android")
    # page.keyboard.press("Enter")
    search_button = page.locator("#gh-search-btn")
    search_button = page.locator("[id='gh-search-btn']")
    text_option_1 = search_button.inner_text()
    text_option_2 = search_button.text_content()
    advanced= page.get_by_role("Link",name="Advanced")
    search.click(position={"x": 1300, "y": 15})
    page.query_selector_all("[class =‘inventory_item_price’]")




    # search_button.click()
    print (page.url)

    browser.close()