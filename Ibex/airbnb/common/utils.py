import calendar
from datetime import datetime, timedelta

class Utils():
    def __init__(self, page):
        self.__page = page

    def get_date_as_string(self, delta) -> dict:
        present_day = datetime.now()
        final_date = present_day + timedelta(delta)
        month = calendar.month_name[final_date.month]
        year = str(final_date.year)
        date = {
            "all":final_date.strftime("%m/%d/%Y"),
            "day": final_date.day,
            "month": month,
            "year": year
        }
        return date

    def demo(self):
        pass
