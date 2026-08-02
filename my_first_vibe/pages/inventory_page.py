from playwright.sync_api import Page, expect


class InventoryPage:
    """Page object for the Saucedemo inventory page (products)."""

    def __init__(self, page: Page):
        self.page = page
        self._prices = page.locator(".inventory_item_price")
        self._items = page.locator(".inventory_item")

    def get_all_prices(self) -> list[float]:
        """Return a list of all product prices as floats."""
        # ensure at least one price is visible
        expect(self._prices.first).to_be_visible()
        texts = self._prices.all_text_contents()
        prices = []
        for t in texts:
            clean = t.strip().lstrip("$")
            try:
                val = float(clean)
            except ValueError:
                raise AssertionError(f"Price text could not be parsed to float: '{t}'")
            prices.append(val)
        return prices

    def count_items(self) -> int:
        """Return the number of inventory items on the page."""
        return self._items.count()
