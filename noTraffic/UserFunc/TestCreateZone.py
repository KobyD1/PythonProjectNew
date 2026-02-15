import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from noTraffic.Pages.CreateZonePage import CreateZonePage
from noTraffic.Pages.GetAllZonesPage import GetAllZonesPage
from noTraffic.Pages.WelcomeNTPage import WelcomeNTPage
from noTraffic.UserFunc import BaseNoTrafic
from noTraffic.UserFunc.BaseNoTrafic import points, api


@pytest.fixture()
def setup_create(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BaseNoTrafic.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    api.delete_all_zones()
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_create")
class TestCreateZone():
    def test_create_single_zone(self):
        welcomePage = WelcomeNTPage(self.driver)
        getPage = GetAllZonesPage(self.driver)
        createPage = CreateZonePage(self.driver)
        zone_name = "test"
        welcomePage.click_on_create_zone()
        createPage.set_zone(zone_name)
        amount = getPage.get_zone_by_name(zone_name)
        assert amount == 1, 'Zone not found as a result of create Zone'

    # not stable
    def test_create_duplicate_zone(self):
        welcomePage = WelcomeNTPage(self.driver)
        createPage = CreateZonePage(self.driver)
        getPage = GetAllZonesPage(self.driver)
        zone_name = "Dup.test"
        for i in range(0, 3):
            welcomePage.click_on_create_zone()
            createPage.set_zone(zone_name)

        amount = getPage.get_zone_by_name(zone_name)
        assert amount == 1, 'Zone not found as expected as  a result of Dup. create Zone'

    # create zone without name cause http = 500, done by set the name to "Zone with no name" - should be improved
    def test_create_noname_zone(self):
        welcomePage = WelcomeNTPage(self.driver)
        createPage = CreateZonePage(self.driver)
        getPage = GetAllZonesPage(self.driver)
        zone_name = "Zone with no name"
        welcomePage.click_on_create_zone()
        createPage.set_zone(zone_name)

        amount = getPage.get_zone_by_name(zone_name)
        assert amount == 1, 'Zone not found as expected as create Zone without name'

    # test to find if create zone button is clickable as default, should be improved to test it after once clicked
    def test_create_zone_clickable(self):
        welcomePage = WelcomeNTPage(self.driver)
        is_clickable = welcomePage.create_zone_is_clickable()
        assert is_clickable == True



    # tests for create zone with user error by points amount(not ready)
    def test_create_zone_by_5points_negative_test(self):
        pass

    def test_create_zone_by_3points_negative_test(self):
        pass

    def test_create_zone_by_names(self):
        welcomePage = WelcomeNTPage(self.driver)
        getPage = GetAllZonesPage(self.driver)
        createPage = CreateZonePage(self.driver)
        welcomePage.click_on_get_all()
        welcomePage.click_on_create_zone()
        pattern = "!@#!@#//||\\"
        createPage.set_zone(pattern)
        amount = getPage.get_zone_by_name(pattern)
        assert amount == 1, 'Test for create zone with special Chars failed '
