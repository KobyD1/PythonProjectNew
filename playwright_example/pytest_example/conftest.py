import pytest
from playwright.sync_api import sync_playwright, expect


expect.set_options(timeout=10_000)


@pytest.fixture()
def setup_playwright():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # welcome_page = welcomePage(page)
        # product_page = productPage(page)
        yield page
        print("### Test end ###")
        page.close()
        browser.close()
