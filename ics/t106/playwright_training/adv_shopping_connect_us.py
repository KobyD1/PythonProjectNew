import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(" https://advantageonlineshopping.com/#/")


    contact_button = page.get_by_role("link",name="CONTACT US")
    contact_text = contact_button.inner_text()
    print (f"contact_text value  = {contact_text}")
    contact_button.click()




    print ("test end")

    browser.close()