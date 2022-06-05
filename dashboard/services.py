from datetime import datetime, date
import calendar

from dashboard.models import SubGoalCompletion


class CalendarService:

    @staticmethod
    def get_calendar(goal):
        now = datetime.now()
        last_day = calendar.monthrange(now.year, now.month)[1]
        number_of_day_in_week = date(now.year, now.month, 1).weekday()
        result_list = []
        temp_list = []
        for i in range(0, 35):
            if i < number_of_day_in_week:
                temp_list.append({"value": "null", "date": "null"})
                continue
            day = i - number_of_day_in_week + 1
            if i > last_day + 1:
                temp_list.append({"value": "null", "date": "null"})
            elif i > now.day + 1:
                temp_list.append({"value": "check", "date": day})
            else:
                if SubGoalCompletion.objects.filter(
                        sub_goal__goal=goal, created_at=date(now.year, now.month, day)).first():
                    temp_list.append({"value": "true", "date": day})
                else:
                    temp_list.append({"value": "false", "date": day})
            if len(temp_list) == 7:
                result_list.append(temp_list)
                temp_list = []
        return result_list
