from playwright.sync_api import expect


class Test_assert_exept:


    def test_assert(self, setup_playwright):



        page = setup_playwright
        page.goto("https://www.ebay.com")
        assert page.url == "https://www.ebay.com/","Page URL is not as expected"
        expect (page).to_have_url("https://www.ebay.com/")

    def test_excpet(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.pizzahut.com/")
        # assert page.url == "https://www.pizzahut.com/","Page URL is not as expected"
        is_visable = page.get_by_role("link",name='Contact us').is_visible()

        assert is_visable == True,"Contact US button is dot displayed"
        expect (page.get_by_role("link",name='Contact us')).not_to_be_hidden()
        assert page.get_by_role("link",name='Contact us').is_visible()