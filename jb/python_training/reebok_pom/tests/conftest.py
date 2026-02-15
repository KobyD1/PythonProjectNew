import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope="session")
def setup_playwright_reebok():
    print (f"starting playwright")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        yield page
        page.close()
        browser.close()
        print("####Test end###")