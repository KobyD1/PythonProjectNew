import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_URL_AFTER_LOGIN = "https://www.saucedemo.com/inventory.html"


def test_read_all_prices_after_login(page: Page):
    """Login, read all product prices on inventory page, and assert they're positive numbers."""
    page.goto(BASE_URL)

    # login
    username = page.locator("#user-name")
    password = page.locator("#password")
    login_button = page.locator("#login-button")

    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(login_button).to_be_visible()

    username.fill(USERNAME)
    password.fill(PASSWORD)
    login_button.click()

    # ensure inventory loaded
    expect(page).to_have_url(EXPECTED_URL_AFTER_LOGIN)

    prices_locator = page.locator(".inventory_item_price")
    expect(prices_locator.first).to_be_visible()

    prices_texts = prices_locator.all_text_contents()
    assert len(prices_texts) > 0, "No prices found on inventory page"

    # parse prices and assert they are positive numbers
    prices = []
    for t in prices_texts:
        # expected format: "$9.99"
        clean = t.strip().lstrip("$")
        try:
            val = float(clean)
        except ValueError:
            pytest.fail(f"Price text could not be parsed to float: '{t}'")
        assert val > 0, f"Price must be positive, got {val}"
        prices.append(val)

    # additional sanity: ensure list length matches number of inventory items
    items = page.locator(".inventory_item")
    assert len(prices) == items.count()
