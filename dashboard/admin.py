from django.contrib import admin

# Register your models here.
from dashboard.models import Goal, GoalMentor, MentorComment, DiaryComment

admin.site.register(Goal)
admin.site.register(GoalMentor)
admin.site.register(MentorComment)
admin.site.register(DiaryComment)
