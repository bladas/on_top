from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from dashboard.models import Goal, DiaryComment, MentorComment
from dashboard.serializers import GoalSerializer, DiaryCommentSerializer, MentorCommentSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class DiaryCommentViewSet(viewsets.ModelViewSet):
    queryset = DiaryComment.objects.all()
    serializer_class = DiaryCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class MentorCommentViewSet(viewsets.ModelViewSet):
    queryset = MentorComment.objects.all()
    serializer_class = MentorCommentSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)
