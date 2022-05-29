from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dashboard.models import Goal, DiaryComment, MentorComment
from dashboard.serializers import GoalSerializer, DiaryCommentSerializer, MentorCommentSerializer, MentorSerializer


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

    def get_queryset(self, **kwargs):
        goal_pk = self.kwargs['goals_pk']
        return self.queryset.filter(goal__pk=goal_pk)


class MentorCommentViewSet(viewsets.ModelViewSet):
    queryset = MentorComment.objects.all()
    serializer_class = MentorCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        goal_pk = self.kwargs['goals_pk']
        return self.queryset.filter(goal__pk=goal_pk)


class MentorView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, **kwargs):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.assign_mentor(request.data['email'], kwargs['goals_id'])
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
