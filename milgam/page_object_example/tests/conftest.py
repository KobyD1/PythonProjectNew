import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def setup_playwright_swaglabs():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")


        yield page
        print("### Test end ###")
        page.close()
        browser.close()
