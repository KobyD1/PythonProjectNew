import pytest
from playwright.sync_api import Page, expect

from my_first_vibe.pages.login_page import LoginPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_URL_AFTER_LOGIN = "https://www.saucedemo.com/inventory.html"


def test_login_with_page_object_model(page: Page):
    """Login using the Page Object Model and verify successful navigation."""
    login_page = LoginPage(page)
    login_page.goto()

    login_page.login(USERNAME, PASSWORD)

    # verify landing page
    expect(page).to_have_url(EXPECTED_URL_AFTER_LOGIN)
