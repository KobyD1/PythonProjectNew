import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_login_and_select_sort_dropdown(page: Page):
    """Login then select the product sort dropdown and verify the selected option."""
    page.goto(BASE_URL)

    username = page.locator("#user-name")
    password = page.locator("#password")
    login_button = page.locator("#login-button")

    # sanity checks
    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(login_button).to_be_visible()

    # login
    username.fill(USERNAME)
    password.fill(PASSWORD)
    login_button.click()

    # select dropdown on inventory page
    sort_select = page.locator("select.product_sort_container")
    expect(sort_select).to_be_visible()

    # choose by visible label and verify selection
    sort_select.select_option(label="Price (low to high)")
    selected_text = page.evaluate("() => document.querySelector('select.product_sort_container').options[document.querySelector('select.product_sort_container').selectedIndex].text")
    assert "Price (low to high)" in selected_text
