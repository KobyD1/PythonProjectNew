import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"


def test_login_without_password_shows_error(page: Page):
    """Negative test: attempting to login without a password should show an error message."""
    page.goto(BASE_URL)

    username_input = page.locator("#user-name")
    password_input = page.locator("#password")
    login_button = page.locator("#login-button")
    error_locator = page.locator(".error-message-container h3")

    # sanity checks
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()
    expect(login_button).to_be_visible()

    # fill only username, leave password empty
    username_input.fill(USERNAME)
    login_button.click()

    # assert error appears and mentions password
    expect(error_locator).to_be_visible()
    error_text = error_locator.text_content()
    assert error_text is not None and ("Password is required" in error_text or "password is required" in error_text)
