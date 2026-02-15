import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from noTraffic.Pages.CreateZonePage import CreateZonePage
from noTraffic.Pages.GetAllZonesPage import GetAllZonesPage
from noTraffic.Pages.WelcomeNTPage import WelcomeNTPage
from noTraffic.UserFunc import BaseNoTrafic
from noTraffic.UserFunc.BaseNoTrafic import points, api


@pytest.fixture(scope="class")
def setup_view(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BaseNoTrafic.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    api.delete_all_zones()

    for i in range(0, 5):
        api.set_zone("name"+str(i))
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_view")
class TestViewZone():
    def test_view_single_zone(self):
        getPage = GetAllZonesPage(self.driver)
        pattern = getPage.get_zone_all_details('name0')
        assert pattern == '1 name0','Zone appears not as expected into zone list line 0 '

    def test_view_multiple_zone(self):
        getPage = GetAllZonesPage(self.driver)
        zone = getPage.get_zone_all_details('name3')
        assert zone == '4 name3','Zone appears not as expected into zone list'

    # not ready
    def test_get_zones_button_clickable(self):
        pass

    # not ready
    def test_polygon_appears_at_list(self):
        pass

