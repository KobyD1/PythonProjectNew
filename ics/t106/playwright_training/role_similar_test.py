from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    search_menu =page.locator('[id="gh-ac"]')
    search_menu.click()
    search_menu.clear()
    search_menu.fill("Shirt Zara")
    search_button = page.get_by_role("button", name="Search").last


    search_button = page.get_by_role("button",name="Search").last
    search_menu = page.get_by_role("button",name="Search").first
    search_button_1 = page.get_by_role("button",name="Search").nth(1)
    search_button_as_list = page.get_by_role("button",name="Search").all()
    search_button_1.click()

    # search_button.click()
    print ("test end")

    browser.close()