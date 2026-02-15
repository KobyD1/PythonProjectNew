class Test_zara():

    def test_ZaraSaleBucket(self, setup_playwright):
        page =setup_playwright
        page.goto("https://www.zara.com")
        page.locator('[data-qa-action="go-to-store"]').click()
        # SB=page.locator("[class='layout-header-action__link layout-header-action__link--type-text link']").click()
        sale_button =page.locator('[data-qa-id="layout-header-go-to-cart"]')
        sale_button_text =sale_button.inner_text()
        print(f"text fuond the value is {sale_button_text}")
        assert "0" in sale_button_text ,"0 was not found in sale bucket text"
