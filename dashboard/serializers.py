from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from dashboard.models import Goal, DiaryComment, MentorComment, GoalMentor, GoalReminding, SubGoal
from on_top.settings import DATETIME_FORMAT

User = get_user_model()


class GoalSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"

    def create(self, validated_data):
        """Creating goal"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)


class SubGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubGoal
        exclude = ['goal']

    def create(self, validated_data):
        """Creating sub goal"""
        kwargs = self.context['request'].parser_context['kwargs']
        validated_data["goal"] = Goal.objects.get(pk=kwargs['goals_pk'])
        return super().create(validated_data)


class DiaryCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = DiaryComment
        exclude = ['user', 'goal']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        kwargs = self.context['request'].parser_context['kwargs']
        validated_data["goal"] = Goal.objects.get(pk=kwargs['goals_pk'])
        validated_data["user"] = user
        return super().create(validated_data)


class MentorCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = MentorComment
        exclude = ['user', 'goal']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        kwargs = self.context['request'].parser_context['kwargs']
        validated_data["goal"] = Goal.objects.get(pk=kwargs['goals_pk'])
        validated_data["user"] = user
        return super().create(validated_data)


class RemindingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = GoalReminding
        exclude = ['user', 'goal']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        kwargs = self.context['request'].parser_context['kwargs']
        validated_data["goal"] = Goal.objects.get(pk=kwargs['goals_pk'])
        validated_data["user"] = user
        return super().create(validated_data)


class MentorSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    @staticmethod
    def validate_email(value):
        """Validating email"""
        users = User.objects.filter(email=value)
        if not users.first():
            raise serializers.ValidationError("Invalid user email")
        return value

    @staticmethod
    def assign_mentor(email, goal_id):
        user = User.objects.get(email=email)
        goal = Goal.objects.get(id=goal_id)
        GoalMentor.objects.create(
            user=user,
            goal=goal
        )

    @staticmethod
    def delete_mentor(email, goal_id):
        user = User.objects.get(email=email)
        goal = Goal.objects.get(id=goal_id)
        GoalMentor.objects.filter(user=user, goal=goal).delete()


class MentorModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GoalMentor
        exclude = ['goal']
