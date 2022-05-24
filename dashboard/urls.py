
from django.urls import path, include
from rest_framework import routers

from dashboard.views import GoalViewSet

router = routers.DefaultRouter()
router.register(r'goals', GoalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
