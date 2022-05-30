from django.urls import path

from accounts.views import UserDetailView

urlpatterns = [
    path('me/', UserDetailView.as_view()),
]
