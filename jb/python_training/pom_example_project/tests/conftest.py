import pytest
from playwright.sync_api import sync_playwright

from jb.python_training.pom_example_project.globals import URL


@pytest.fixture(scope="session")
def setup_playwright_project():
    print (f"starting playwright")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        yield page
        page.close()
        browser.close()
        print("####Test end###")