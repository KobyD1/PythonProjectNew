from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.ebay.com")
    print(page.title())
    search = page.locator('#gh-ac')

    search.dblclick()
    search.type("Phone2")
    cart  = page.locator('svg.gh-cart-icon')
    cart.hover()
    assert page.title() == "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
    print ('Test end')
    browser.close()