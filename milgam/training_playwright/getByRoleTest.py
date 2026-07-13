import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    contact_us = page.get_by_role("link",name = 'CONTACT')
    contact_us.click()
    # get by role usefull values
    #     button
    #    link
    #    textbox
    #    combobox
    #     checkbox
    #     radio
    #     heading

    url = page.url




    browser.close()