from rest_framework import serializers

from dashboard.models import Goal, DiaryComment, MentorComment
from on_top.settings import DATETIME_FORMAT


class GoalSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = Goal
        exclude = ['user']

    def create(self, validated_data):
        """Creating goal"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)


class DiaryCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = DiaryComment
        exclude = ['user']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)


class MentorCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None, read_only=True)

    class Meta:
        model = MentorComment
        exclude = ['user']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)
