from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")

    contact_button = page.get_by_role("link",name="Contact")
    contact_button.click()



    page.close()