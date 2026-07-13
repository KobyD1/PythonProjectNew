



@pytest.fixture()
def setup_playwright():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()


        yield page
        print("### Test end ###")
        page.close()
        browser.close()
