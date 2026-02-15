from noTraffic.Utils.APIutils import APIutils
# common class for all common parameters
url = 'http://54.73.80.13:8000/main'
url_api_prefix = 'http://54.73.80.13:5000'
points = [{124, 44}, {205, 44}, {198, 63}, {126, 59}]
api = APIutils(url_api_prefix)
zone = {
    "id": 1,
    "name": "temp",
    "points": [[124, 44], [205, 44], [198, 63], [126, 59]]
}

headers = {'Content-Type': 'application/json'}





