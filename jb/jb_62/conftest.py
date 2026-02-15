import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def setup_playwright(base_url):
    print (f"starting playwright into url {base_url} ")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        # page.goto("https://www.saucedemo.com/")
        yield page
        page.close()
        browser.close()
        print("####Test end###")