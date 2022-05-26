
from django.urls import path, include
from rest_framework import routers

from dashboard.views import GoalViewSet, DiaryCommentViewSet, MentorCommentViewSet

router = routers.DefaultRouter()
router.register(r'goals', GoalViewSet)
router.register(r'author-comments', DiaryCommentViewSet)
router.register(r'mentor-comments', MentorCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
