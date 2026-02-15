from playwright.sync_api import expect

from jb.python_training.pom_example_project.globals import URL, ITEM_TO_FIND
from jb.python_training.pom_example_project.pages.adv_page import AdvPage
from jb.python_training.pom_example_project.pages.search_page import SearchPage


class TestEbayTest:

    def test_search_for_camera(self,setup_playwright_project):
        page = setup_playwright_project
        search_page = SearchPage(page)
        search_page.search_for_item("shoes men reabok white with ")
        text = search_page.get_amount_after_search()
        assert int(text) >100,"products did not found "

    def test_click_on_adv_button(self,setup_playwright_project):
        page = setup_playwright_project
        search_page = SearchPage(page)
        search_page.click_on_advanced_link()
        expect (page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")
        assert page.title()=="Advanced Search | eBay", "Page title is not as expected after click_on_advanced_link"

    def test_search_from_adv_page(self,setup_playwright_project):
        page = setup_playwright_project
        adv_page = AdvPage(page)
        search_page = SearchPage(page)
        search_page.click_on_advanced_link()
        adv_page.search_for_item(ITEM_TO_FIND)
        text = search_page.get_amount_after_search()
        assert int(text) > 100, "products did not found "
