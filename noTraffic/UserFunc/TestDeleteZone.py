import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from noTraffic.Pages.GetAllZonesPage import GetAllZonesPage
from noTraffic.Pages.WelcomeNTPage import WelcomeNTPage
from noTraffic.UserFunc import BaseNoTrafic
from noTraffic.UserFunc.BaseNoTrafic import api


@pytest.fixture(scope="class")
def setup_delete(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BaseNoTrafic.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    api.delete_all_zones()
    for i in range(0, 5):
        api.set_zone("name" + str(i))

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_delete")
class TestDeleteZone():

    def test_delete_first_zone(self):
        welcomePage = WelcomeNTPage(self.driver)
        getPage = GetAllZonesPage(self.driver)

        welcomePage.click_on_get_all()
        zone_before = getPage.delete_zone_by_line(0)
        amount = getPage.get_zone_by_name(zone_before)
        assert amount == 0, 'Zone  found  as a result of delete Zone in line 0 '

    def test_delete_any_zone(self):
        welcomePage = WelcomeNTPage(self.driver)
        getPage = GetAllZonesPage(self.driver)
        line_to_del = 3
        welcomePage.click_on_get_all()

        zone_before = getPage.delete_zone_by_line(line_to_del)
        amount = getPage.get_zone_by_name(zone_before)
        assert amount == 0, 'Zone  found  as a result of delete Zone in line  ' + str(line_to_del)

   # not ready
    def test_delete_all_zones(self):
        pass
