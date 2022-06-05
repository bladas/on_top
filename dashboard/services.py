from datetime import datetime, date
import calendar


class CalendarService:

    def get_calendar(self):
        now = datetime.now()
        last_day = calendar.monthrange(now.year, now.month)[1]
        number_of_day_in_week = date(now.year, now.month, 1).weekday()
        result_list = []
        d = dict()
        for i in range(0, 34):
            if i > number_of_day_in_week:
                d['-'] = "null"
            # if
            d[str(i)] = "true"
