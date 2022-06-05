from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dashboard.models import Goal, DiaryComment, MentorComment, GoalMentor, GoalReminding, SubGoal, SubGoalCompletion
from dashboard.serializers import GoalSerializer, DiaryCommentSerializer, MentorCommentSerializer, MentorSerializer, \
    MentorModelSerializer, RemindingSerializer, SubGoalSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    filterset_fields = ['title']

    def get_queryset(self):
        query_params = self.request.query_params
        user = self.request.user
        if query_params.get('search') or self.request.method == "GET":
            return self.queryset.filter(Q(is_private=False) | Q(user=user))
        return self.queryset.filter(user=user)


class SubGoalViewSet(viewsets.ModelViewSet):
    queryset = SubGoal.objects.all()
    serializer_class = SubGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        goal_pk = self.kwargs['goals_pk']
        user = self.request.user
        return self.queryset.filter(goal__pk=goal_pk, goal__user=user)


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


class RemindingViewSet(viewsets.ModelViewSet):
    queryset = GoalReminding.objects.all()
    serializer_class = RemindingSerializer
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
            serializer.assign_mentor(request.data['email'], kwargs['goals_pk'])
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, **kwargs):
        mentors = GoalMentor.objects.filter(goal__pk=kwargs['goals_pk'])
        serializer = MentorModelSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, **kwargs):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete_mentor(request.data['email'], kwargs['goals_pk'])
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubGoalCompletionView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, **kwargs):
        SubGoalCompletion.objects.create(
            sub_goal=SubGoal.object.get(pk=kwargs['sub_goals_pk'])
        )
        return Response(status=status.HTTP_200_OK)


class CalendarView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, **kwargs):
        mentors = GoalMentor.objects.filter(goal__pk=kwargs['goals_pk'])
        serializer = MentorModelSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
