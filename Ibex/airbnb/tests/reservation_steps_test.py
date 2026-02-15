import pytest

from Ibex.airbnb.tests.globals import  main_search, guest_test_search, dates_test_search


@pytest.mark.flaky(reruns=2)
class TestAirbnb():

    def test_search_main(self, setup_browser):
        common_pages, results_page, place_page, payment_page = setup_browser
        common_pages.set_search_details(main_search)
        high_rate_index = results_page.get_and_sort_place_data()
        results_page.get_room_by_href(high_rate_index)
        place_page.get_and_assert_booking_details(main_search)
        place_page.click_on_reserved()
        payment_page.get_and_assert_url(main_search)
        print("Test End")

    def test_decrease_childrens(self, setup_browser):
        common_pages, results_page, place_page, payment_page = setup_browser
        common_pages.set_search_details(main_search)
        high_rate_index = results_page.get_and_sort_place_data()
        results_page.get_room_by_href(high_rate_index)
        place_page.prapare_to_search_guests()
        common_pages.set_guests(guest_test_search["adults"], guest_test_search["children"])
        common_pages.click_on_search()

        high_rate_index = results_page.get_and_sort_place_data()
        results_page.get_room_by_href(high_rate_index)
        place_page.get_and_assert_booking_guests(guest_test_search)
        print("Test End")

    def test_change_dates(self, setup_browser):
        common_pages, results_page, place_page, payment_page = setup_browser
        common_pages.set_search_details(main_search)
        rate_index_before = results_page.get_and_sort_place_data()
        results_page.get_room_by_href(rate_index_before)
        place_page.prapare_to_search_dates()
        common_pages.set_dates(dates_test_search["from_delta"], dates_test_search["to_delta"])
        common_pages.click_on_search()
        rate_index_after = results_page.get_and_sort_place_data()
        if (rate_index_after == -1):
            print("return to preliminary search due places not found")
            common_pages.set_search_details(main_search)

        results_page.get_room_by_href(rate_index_after)
        place_page.get_and_assert_booking_dates(dates_test_search)
        print("Test End")
