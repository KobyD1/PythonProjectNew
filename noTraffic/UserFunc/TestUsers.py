import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from noTraffic.UserFunc import BaseNoTrafic
from noTraffic.UserFunc.BaseNoTrafic import api


@pytest.fixture()
def setup_e2e(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BaseNoTrafic.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    api.delete_all_zones()
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_e2e")
class TestUsers():

# user1 create zone , user2 can watch all zone details
    def zone_can_watch_by_all_users(self):
        pass

# user 1 delete zone and user 2 create the same zone
    def create_after_delete_same_zone(self):
        pass

# user 1 create zone and user 2 create the same zone
    def create_same_zone(self):
        pass