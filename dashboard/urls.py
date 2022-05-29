
from django.urls import path, include
from rest_framework import routers

from dashboard.views import GoalViewSet, DiaryCommentViewSet, MentorCommentViewSet

router = routers.DefaultRouter()
router.register(r'goals', GoalViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/author-comments', DiaryCommentViewSet)
router.register(r'goals/(?P<goals_pk>\d+)/mentor-comments', MentorCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
