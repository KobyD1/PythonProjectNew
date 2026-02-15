from playwright.sync_api import expect
from retry import retry


class transactionsPage():
    def __init__(self, page):
        self.__page = page
        self.__reset_button = self.__page.get_by_text("Reset")
        self.__back_button = self.__page.get_by_text("Back")
        self.__table = self.__page.locator("table.table.table-bordered.table-striped")

    def reset_table_and_back(self):
        if (self.__reset_button.is_visible()):
            self.__reset_button.click()
        rows =self.__page.query_selector_all("tr")
        assert len(rows) == 0 , "Rows are still appears into Transactions table after reset "
        self.__back_button.click()

    @retry(exceptions=AssertionError, tries=5, delay=1)
    def get_table_row_data(self, row_index: int) -> dict:
        row_data = {}
        expect(self.__back_button).to_be_visible()
        rows = self.__page.query_selector_all("tr")

        assert len(rows) > 1 , "Rows not found into Transactions table as expected "
        row = rows[row_index]
        cells = row.query_selector_all("td")
        row_data["date"] = cells[0].text_content()
        row_data["amount"] = cells[1].text_content()
        row_data["type"] = cells[2].text_content()
        print (f"the following row data found {row_data}")
        return row_data

    def get_table_rows_amount (self):
        rows = self.__page.query_selector_all("tr")
        print (f'Rows found = {len(rows)}')
        if ({len(rows)} ==1 ):
            self.__back_button.click()
        return len(rows)




