import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")
    help_button = page.get_by_role("link",name= "HELP")
    help_button.click()




    print ("test end")

    browser.close()