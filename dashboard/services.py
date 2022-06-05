from datetime import datetime
import calendar


class CalendarService:

    def get_calendar(self):
        now = datetime.now()
        print(calendar.monthrange(now.year, now.month))
        print(datetime.date(now.year, now.month, 1).weekday())
