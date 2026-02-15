from noTraffic.Pages.Locators import CreateZonePageLocetors
from noTraffic.UserFunc.BaseNoTrafic import url_api_prefix
from noTraffic.Utils.APIutils import APIutils


class CreateZonePage(object):

    def __init__(self, driver):
        self.driver = driver

    api = APIutils(url_api_prefix)

    # method for set zone name
    def set_name(self, pattern):
        name = self.driver.find_element(*CreateZonePageLocetors.NAME)
        name.click()
        name.clear()
        name.send_keys(pattern)

    # method for set zone name full process

    def set_zone(self, name):
        self.set_name(name)
        self.api.set_zone(name)
