import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    search_button = page.locator("[id='menuSearch']")
    search_button.click()

    search_menu = page.locator("#autoComplete")
    search_menu.click()
    search_menu.fill(" Shirt")
    search_menu.press("Enter")







    browser.close()