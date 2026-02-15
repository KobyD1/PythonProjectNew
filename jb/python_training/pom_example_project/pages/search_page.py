import time

from playwright.sync_api import expect


class SearchPage():

    def __init__(self, page):
        self.page = page

    def search_for_item(self,item:str):
        search_menu= self.page.locator("[id='gh-ac']")
        search_menu_short= self.page.locator("#gh-ac")

        search_menu.click()
        search_menu.fill(item)

        self.page.get_by_role("button",name="Search").click()

    def get_amount_after_search(self):
        print ("trying to get result")
        time.sleep(3)  # adding sleep since slow response after search
        text_element  = self.page.locator("[class='s-answer-region s-answer-region-center-top']")


        text = text_element.inner_text()
        # if "+" in text:
        #     index= text.index("+")
        #     text = text[:index]

        text=text.replace("+","")
        text=text.replace(",","")

        # if "+" not in text:
        index= text.index("results")
        text = text[:index]

        print (f"result text is {text}")
        return text

    def click_on_advanced_link(self):
        adv_button = self.page.get_by_role("link",name= "Advanced")
        adv_button.click()

