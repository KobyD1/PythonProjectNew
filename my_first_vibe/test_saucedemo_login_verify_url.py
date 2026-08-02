import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_URL_AFTER_LOGIN = "https://www.saucedemo.com/inventory.html"


def test_login_verify_by_url(page: Page):
    """Verify successful login by checking the resulting page URL."""
    page.goto(BASE_URL)
    username = page.locator("#user-name")
    password = page.locator("#password")
    login_button = page.locator("#login-button")

    # sanity checks
    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(login_button).to_be_visible()

    # perform login
    username.fill(USERNAME)
    password.fill(PASSWORD)
    login_button.click()

    # verify URL changed to inventory page
    expect(page).to_have_url(EXPECTED_URL_AFTER_LOGIN)
