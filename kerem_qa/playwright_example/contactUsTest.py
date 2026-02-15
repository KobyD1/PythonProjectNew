from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/https://advantageonlineshopping.com/#/")
    # contact_us = page.locator("[href='javascript:void(0)']")
    # contact_us.click()
    category = page.locator("[name='categoryListboxContactUs']")
    category.select_option(index=1)
    email = page.locator("[name='emailContactUs']")
    email.fill("abc@abc.com")
    subject  = page.locator("[name='subjectTextareaContactUs']")
    subject.fill("Hi , pleas provide details")
    send= page.locator("[id='send_btn']")
    send.click()
    continue_button = page.get_by_text("CONTINUE SHOPPING")

    text = continue_button.all_inner_texts()
    assert "CONTINUE SHOPPING" in text[0],"text is not as expected into continue button "
    continue_button.click()
    is_pass = not (continue_button.is_visible())
    assert is_pass, "conitue button appears not as expected"


    browser.close()