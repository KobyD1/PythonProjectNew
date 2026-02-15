import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from noTraffic.UserFuncUI import BaseNoTrafic


@pytest.fixture(scope="class")
def setup_e2e(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BaseNoTrafic.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_e2e")
class TestE2E():

    def test_e2e(self):
        pass