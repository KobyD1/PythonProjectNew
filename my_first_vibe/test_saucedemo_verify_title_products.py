import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_login_and_verify_title_products(page: Page):
    """Login to saucedemo and verify the inventory page title reads 'Products'."""
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

    # verify page title
    title_locator = page.locator(".title")
    expect(title_locator).to_be_visible()
    expect(title_locator).to_have_text("Products")
