BASE_URL = "http://www.airbnb.com"
LOCATION = "Amsterdam, Netherlands"
EXP_ADULTS = 2
EXP_CHILDREN = 1
FROM_DELTA = 1  # checkin day range from today (in days)
BROWSER = 1  # 1- for Chrome , 2- for Firefox
main_search = {
    "location": LOCATION,
    "from_delta": FROM_DELTA,
    "to_delta": FROM_DELTA + 1,
    "adults": EXP_ADULTS,
    "children": EXP_CHILDREN
}

dates_test_search = {
    "location": LOCATION,
    "from_delta": FROM_DELTA,
    "to_delta": FROM_DELTA + 7,
    "adults": EXP_ADULTS,
    "children": EXP_CHILDREN
}

guest_test_search = {
    "location": LOCATION,
    "from_delta": FROM_DELTA,
    "to_delta": FROM_DELTA + 1,
    "adults": EXP_ADULTS,
    "children": 0
}
