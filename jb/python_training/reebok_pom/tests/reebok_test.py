from jb.python_training.reebok_pom.pages.resultsPage import ResultsPage
from jb.python_training.reebok_pom.pages.welcomePage import WelcomePage


class TestReebokTest():

    def test_search_for_item_and_getting_results(self,setup_playwright_reebok):
        page = setup_playwright_reebok
        result_page = ResultsPage(page)
        welcome_page =WelcomePage(page)
        page.goto("https://www.reebok.com/")
        welcome_page.click_on_close_popup()
        welcome_page.search_for_item()
        result_page.get_text_from_results()
