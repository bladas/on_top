from django.urls import path, include
from rest_framework import routers

from dashboard.views import GoalViewSet, DiaryCommentViewSet, MentorCommentViewSet, MentorView, RemindingViewSet, \
    SubGoalViewSet, SubGoalCompletionView, CalendarView

router = routers.DefaultRouter()
router.register(r'goals', GoalViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/author-comments', DiaryCommentViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/mentor-comments', MentorCommentViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/reminding', RemindingViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/sub-goals', SubGoalViewSet)

urlpatterns = [
    path('goals/<int:goals_pk>/mentor/', MentorView.as_view()),
    path('goals/<int:goals_pk>/sub-goals/<int:sub_goals_pk>/approve', SubGoalCompletionView.as_view()),
    path('goals/<int:goals_pk>/calendar/', CalendarView.as_view()),
    path('', include(router.urls)),
]
