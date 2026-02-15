# in the test
from playwright.sync_api import sync_playwright

from Examples.PlayWright.pageObject.pages.SearchPage import SearchPage

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")