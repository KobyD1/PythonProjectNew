from playwright.sync_api import expect


class ResultsPage:
    def __init__(self, page):
        self.__page = page
        self.__result_pattern = page.locator("[id='result-stats']")

    def get_results(self)->str:
        expect(self.__result_pattern).to_be_visible()
        text = self.__result_pattern.text_content()
        index_end = text.index(" ")
        index_start = text.index("-")
        amount = text[index_start:index_end]
        return amount

