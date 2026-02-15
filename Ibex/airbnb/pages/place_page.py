

from playwright.sync_api import expect
from Ibex.airbnb.common.utils import Utils


class placePage:
    def __init__(self, page):
        self.__page = page
        self.__main_buttons_locator = "div.c1yo0219.dir.dir-ltr"
        self.__checkin_button = self.__page.get_by_test_id("change-dates-checkIn")
        self.__checkout_button = self.__page.get_by_test_id("change-dates-checkOut")
        self.__guests_button = self.__page.locator("[id='GuestPicker-book_it-trigger']")
        self.__search_guest = self.__page.get_by_role("button", name="Guests 3 guests")
        self.__search_dates_selector = "div.f16sug5q.dir.dir-ltr"
        self.__clear_dates = self.__page.get_by_role("button", name="Clear Input")
        self.___reserved = self.__page.get_by_test_id("homes-pdp-cta-btn").last
        self.__utils = Utils(self.__page)

    def get_and_assert_booking_details(self, exp_details: dict):
        self.get_and_assert_booking_dates(exp_details)
        self.get_and_assert_booking_guests(exp_details)

    def get_and_assert_booking_dates(self, exp_details: dict):
        date_from = self.__utils.get_date_as_string(exp_details["from_delta"])
        date_to = self.__utils.get_date_as_string(exp_details["to_delta"])
        checkin = self.__checkin_button.text_content()
        checkout = self.__checkout_button.text_content()
        date_from["all"] = self.prapare_date_to_compare(date_from["all"])
        date_to["all"] = self.prapare_date_to_compare(date_to["all"])
        assert (checkin,checkout) == (date_from["all"],date_to["all"]), "One or more checkout or checkin details is not as defined"


    def get_and_assert_booking_guests(self, exp_details: dict):
        act_guests = self.__guests_button.text_content()
        index_guests = act_guests.index(" ")
        act_guests_as_int = int(act_guests[:index_guests])
        exp_guests = exp_details["adults"] + exp_details["children"]
        assert act_guests_as_int >= exp_guests, "Guest amount into reservation is not as defined "

    def click_on_reserved(self):
        print ("Reservation details setting success - navigate to payment page")
        self.___reserved.click()

    def prapare_to_search_guests(self):
        self.__page.go_back()
        self.__search_guest.click()

    def prapare_to_search_dates(self):
        self.__page.go_back()
        expect(self.__search_guest).to_be_visible()
        self.__page.query_selector_all(self.__search_dates_selector)[1].click()
        self.__clear_dates.click()

    def prapare_date_to_compare(self,date:str)->str:
        if ("/0" in date):
            date = date.replace("/0", "/")
        if (date[0] == "0"):
            date = date[1:]
        return date
