import pytest
from playwright.sync_api import Page, expect

from my_first_vibe.pages.login_page import LoginPage
from my_first_vibe.pages.inventory_page import InventoryPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_URL_AFTER_LOGIN = "https://www.saucedemo.com/inventory.html"


def test_read_prices_via_pom(page: Page):
    """Login via POM and read all product prices using InventoryPage."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USERNAME, PASSWORD)

    # ensure inventory loaded
    expect(page).to_have_url(EXPECTED_URL_AFTER_LOGIN)

    inventory = InventoryPage(page)
    prices = inventory.get_all_prices()

    assert len(prices) > 0, "No prices found via POM"
    for p in prices:
        assert p > 0, f"Price must be positive, got {p}"

    # sanity: number of prices equals number of items
    assert len(prices) == inventory.count_items()
