from playwright.sync_api import sync_playwright, expect

from kerem_qa.playwright_example.utils.playwright_utils import PlaywrightUtils

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/https://advantageonlineshopping.com/#/")
    playwright_utils = PlaywrightUtils()
    # contact_us = page.locator("[href='javascript:void(0)']")
    # contact_us.click()
    category = page.locator("[name='categoryListboxContactUs']")
    category.select_option(index=1)
    is_name_exist = playwright_utils.is_button_exists(page.locator("[name='emailContactUsdddddd']"))
    assert not is_name_exist

    subject  = page.locator("[name='subjectTextareaContactUs']")
    subject.fill("Hi , pleas provide details")
    send= page.locator("[id='send_btn']")



    browser.close()
    print ("test end")