
class Test_Demoblaze():
    def test_close(self ,setup_playwright):
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")

        contact = page.get_by_role("link" ,name="contact")
        contact.click()
        close_buttons = page.query_selector_all('[class="btn btn-secondary"]')
        # sometimes we should replace space with dot
        close_buttons_replace_space = page.query_selector_all('[class="btn.btn-secondary"]')
        # in case we want to find the class with include and not accurate string
        close_buttons_include = page.query_selector_all('[class*="tn-secondary"]')
        # example of replace class with dot
        close_buttons = page.query_selector_all(".btn btn-secondary")

        close_buttons[0].click()
        print("test over")
