from playwright.sync_api import expect
from retry import retry
from Ibex.airbnb.tests.globals import BASE_URL


class resultsPage:
    def __init__(self, page):
        self.__page = page
        self.__place_data_selector = "div.cy5jw6o.dir.dir-ltr"
        self.__place_href_selector = "a.rfexzly.dir.dir-ltr"
        self.__filter_button = self.__page.get_by_text("Filters")
        self.__place_container_selector = "[data-testid='card-container']"

    def get_and_sort_place_data(self) -> int:
        expect(self.__filter_button).to_be_visible()
        index = 0
        high_rate = 0.0
        places_data = self.__page.query_selector_all(self.__place_container_selector)

        if (len(places_data) < 1):
            print(f"Empty list found as a result of search ")
            high_index = -1

        else:
            for place_data in places_data:
                index += 1
                room_text = place_data.text_content()
                if (("(" in room_text) and ("breakdown" in room_text)):  # some cases are not include rates
                    index_end = room_text.rindex("(") - 1
                    index_start = room_text.index("breakdown") + 9
                    room_rate = room_text[index_start:index_end]
                    rate_as_float = float(room_rate)
                    if (rate_as_float > high_rate):
                        high_rate = rate_as_float
                        high_index= index
        print(f"Found high place in rate of {high_rate} , index = {high_index}")
        return high_index

    def click_on_room_by_index(self, index: int):
        rooms_data = self.__page.query_selector_all(self.__place_data_selector)
        rooms_data[index].click()

    @retry(exceptions=AssertionError, tries=5, delay=1)
    def get_room_by_href(self, index=0):
        places_data = self.__page.query_selector_all(self.__place_href_selector)
        assert len(places_data) > 0, "places not found as a results of searching"
        href = places_data[index].get_attribute("href")
        link = BASE_URL + href
        self.__page.goto(link)
