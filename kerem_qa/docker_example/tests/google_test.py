from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

def test_google():
    print ("### test_google started ###")
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )

    driver.get("https://www.primark.com/en-gb")
    assert driver.current_url == "https://www.primark.com/en-gb"

    driver.quit()
    print ("### test_google end ###")
