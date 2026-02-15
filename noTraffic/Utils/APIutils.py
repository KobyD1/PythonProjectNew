import json

import requests

from noTraffic.UserFunc import BaseNoTrafic


class APIutils():

    def __init__(self, url):
        self.url = url

    # delete all zones in order to get clean Env.
    def delete_all_zones(self):
        response = requests.delete(self.url + '/zones')
        assert response.status_code == 200, 'delete  zone by API failed '

    # set zone with default points .
    def set_zone(self, name_pattern):
        zone = BaseNoTrafic.zone
        zone['name'] = name_pattern
        response = requests.post(self.url + '/zones', headers=BaseNoTrafic.headers, data=json.dumps(zone))
        assert response.status_code == 201, 'create zone by API failed '

    # get zones data (not full ready)
    def get_zones(self):
        response = requests.get(self.url + '/zones')
        assert response.status_code == 201, 'get zone by API failed '
