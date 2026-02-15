from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")

    contact_us_button = page.get_by_text("SPECIAL OFFER")
    contact_us_button.click()


    browser.close()
    print ("Test End")