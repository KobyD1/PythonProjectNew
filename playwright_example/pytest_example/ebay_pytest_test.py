import re


class TestEbayPytest():


    def test_ebay_navigation(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        url = page.url
        assert url == "https://www.ebay.com/","URL is not as expected after navigation"

    def test_search_shoes(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        search_menu = page.locator("[id='gh-ac']")
        search_menu = page.locator("#gh-ac")

        search_button  =page.locator("[id='gh-search-btn']")
        search_menu.click()
        search_menu.type("Shoes")
        search_button.click()

    def test_get_by_role(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        search_menu = page.locator("[id='gh-ac']")
        search_menu.click()
        search_menu.fill("Chair")
        search_button =page.get_by_role("button", name="Search")
        search_button.click()
        print("test end")







    def test_checkbox(self,setup_playwright):
        page = setup_playwright
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        adv = page.get_by_text('Advanced')
        adv.click()
        title = page.locator("[id='s0-1-17-5[1]-[0]-LH_TitleDesc']")
        is_title_selected = title.is_checked()
        if (not is_title_selected):
            title.click()
        print ("Test point")






