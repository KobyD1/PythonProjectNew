import time


class TestEbay:

    def test_ebay_advanced(self,setup_playwright):

        page = setup_playwright
        page.goto("https://www.ebay.com/")
        adv= page.get_by_role("link", name= "Advanced")
        adv.click()
        assert page.title() == "Advanced Search | eBay"
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","Page URL is not correct after click on Adv. button"


    def test_ebay_drop_down_example(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        adv = page.get_by_role("link", name="Advanced")
        adv.click()
        drop_down = page.locator("[id='s0-1-20-4[0]-7[3]-_sacat']")
        time.sleep(3)
        drop_down.select_option("Art")
        drop_down.select_option(index=2)
        print ("Test end")

    def test_ebay_checkbox_example(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        adv = page.get_by_role("link", name="Advanced")
        adv.click()

        sold_checkbox = page.locator("[name='LH_Sold']")
        sold_checkbox.click()
        new_radio = page.get_by_role("radio", name="New")
        new_radio.click()
        print ("Test end")
