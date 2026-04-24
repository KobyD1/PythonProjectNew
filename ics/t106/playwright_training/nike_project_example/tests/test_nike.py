from ics.t106.playwright_training.nike_project_example.pages.page_welcome_nike import PageWelcomeNike


def test_find_product(setup_playwright_nike):
    page = setup_playwright_nike
    page.goto("https://www.nike.com/il/")
    page_welcome = PageWelcomeNike(page)

