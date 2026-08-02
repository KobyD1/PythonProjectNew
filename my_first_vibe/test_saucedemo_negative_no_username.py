import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


def test_login_without_username_shows_error(page: Page):
    """Negative test: attempting to login without a username should show an error message."""
    page.goto(BASE_URL)

    username_input = page.locator("#user-name")
    password_input = page.locator("#password")
    login_button = page.locator("#login-button")
    error_locator = page.locator(".error-message-container h3")

    # sanity checks
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()
    expect(login_button).to_be_visible()

    # fill only password, leave username empty
    password_input.fill(PASSWORD)
    login_button.click()

    # assert error appears and mentions username
    expect(error_locator).to_be_visible()
    error_text = error_locator.text_content()
    assert error_text is not None and ("Username is required" in error_text or "username is required" in error_text or "Epic sadface" in error_text)
