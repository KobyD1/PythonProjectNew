

class TestAdvDemo():

    def test_select_category(self,setup_playwright):
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com/#/")
        contact = page.get_by_text("CONTACT US")
        contact.click()
        category_menu = page.locator("[name='categoryListboxContactUs']")
        category_menu.select_option("Mice")

        category_menu.select_option(index=2)
        text = category_menu.text_content()
        assert text =="Mice"
        print ("test here")
