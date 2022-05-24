from rest_framework import viewsets

from dashboard.models import Goal
from dashboard.serializers import GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
