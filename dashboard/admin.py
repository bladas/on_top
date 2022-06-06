from django.contrib import admin

# Register your models here.
from dashboard.models import Goal, GoalMentor, MentorComment, DiaryComment, SubGoal, GoalReminding, SubGoalCompletion

admin.site.register(Goal)
admin.site.register(GoalMentor)
admin.site.register(MentorComment)
admin.site.register(DiaryComment)
admin.site.register(GoalReminding)
admin.site.register(SubGoal)
admin.site.register(SubGoalCompletion)
