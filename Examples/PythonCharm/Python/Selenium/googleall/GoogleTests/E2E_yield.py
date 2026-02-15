import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver



class TestExampleOne:
    def test_title(self):
        print('into test 1')

    @pytest.mark.usefixtures("setup")  # define here at class level,can be define at test level as well
    def test_google(self):
        print("Verify content on the page")
        self.driver.find_element(By.NAME, "q").send_keys("hhhhh")

