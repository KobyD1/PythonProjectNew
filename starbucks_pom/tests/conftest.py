import pytest
from playwright.sync_api import sync_playwright, expect

from starbucks_pom.pages.find_store_page import findStoreStarbucksPage
from starbucks_pom.pages.welcome_page import welcomeStarbucksPage

expect.set_options(timeout=10_000)


@pytest.fixture()
def setup_starbucks():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.starbucks.com/")

        welcome_page = welcomeStarbucksPage(page)
        store_page = findStoreStarbucksPage(page)

        yield page,welcome_page,store_page
        print("### Test end ###")
        page.close()
        browser.close()
