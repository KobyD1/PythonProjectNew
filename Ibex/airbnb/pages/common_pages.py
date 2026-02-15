import time

from playwright.sync_api import expect
from Ibex.airbnb.common.utils import Utils


class commonPages:
    def __init__(self, page):
        self.__page = page
        self.__search_button = self.__page.get_by_text("Anywhere")
        self.__add_guests_button = self.__page.get_by_text("GuestsAdd guests")
        self.__start_search = self.__page.get_by_text("Start your search")
        self.__guests_button = self.__page.get_by_test_id("structured-search-input-field-guests-button")
        self.__date_button = self.__page.get_by_test_id("structured-search-input-field-split-dates-0")
        self.__increase_adults = self.__page.locator("button[data-testid='stepper-adults-increase-button']")
        self.__increase_children = self.__page.get_by_test_id('stepper-children-increase-button')
        self.__decrease_children = self.__page.get_by_test_id('stepper-children-decrease-button')
        self.__adults_value = self.__page.get_by_test_id('stepper-adults-value')
        self.__children_value = self.__page.get_by_test_id('stepper-children-value')
        self.__where_button = self.__page.locator("[id='bigsearch-query-location-input']")
        self.__search_icon = self.__page.get_by_test_id('structured-search-input-search-button')
        self.__translator_icon = self.__page.locator("button.cqfm6nt.c177491c.dir.dir-ltr")
        self.__auto_translate = self.__page.locator("div.s195dsor.sl9yi1h.dir.dir-ltr")
        self.__utils = Utils(self.__page)

    def set_search_details(self, search_details: dict):
        self.set_location(search_details["location"])
        self.set_dates(search_details["from_delta"], search_details["to_delta"])
        self.set_guests(search_details["adults"], search_details["children"])
        self.click_on_search()

    def set_location(self, pattern: str):
        print(f"Try to set location to {pattern}")
        expect(self.__search_button).to_be_visible()
        self.__search_button.click()
        self.__where_button.fill(pattern)
        self.__where_button.press("Enter")

    def set_dates(self, from_delta: int, to_delta: int):
        print(f"Try to set dates according :from = +{from_delta} day/s , to = +{to_delta} day/s  ")
        expect(self.__date_button).to_be_visible()
        self.__date_button.click()
        self.set_date(from_delta, True)
        self.set_date(to_delta, True)

    def set_date(self, delta: int, is_current_month: bool):
        date = self.__utils.get_date_as_string(delta)
        act_month = self.__page.get_by_text(date["month"] + " " + date["year"])
        if act_month.is_visible():
            print(f"Month and year appears into select date menu")
        else:
            assert False("Dates are not visible - please change your time range")

        date_pattern = date["all"]
        day_element = self.__page.get_by_test_id(f"calendar-day-{date_pattern}")
        day_element.click()

    def click_on_search(self):
        self.__search_icon.click()
        expect(self.__search_icon).not_to_be_visible()
        time.sleep(3)  # the smart wait is not stable

    def set_guests(self, exp_adults: int, exp_children: int):
        print(f"Try to set guests according adults ={exp_adults}, children = {exp_children}")
        if (self.__children_value.count() == 0):
            self.__guests_button.click()

        act_adults = self.__adults_value.text_content()
        act_children = self.__children_value.text_content()
        adults_delta = exp_adults - int(act_adults)
        children_delta = exp_children - int(act_children)
        print(f"set new guests values ,according adults ={adults_delta}, children = {children_delta}")

        for i in range(adults_delta):
            self.__increase_adults.click()

        if (children_delta > 0):
            for i in range(children_delta):
                self.__increase_children.click()

        elif (children_delta < 0):
            for i in range(abs(children_delta)):
                self.__decrease_children.click()

        else:
            print("Children amount is as expected")

        self.__guests_button.click()

    def set_translator(self):
        self.__translator_icon.click()
        self.__auto_translate.click()
        expect(self.__auto_translate).not_to_be_visible()
        time.sleep(3)
