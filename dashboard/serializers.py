from rest_framework import serializers

from dashboard.models import Goal, DiaryComment, MentorComment


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        exclude = ['user']

    def create(self, validated_data):
        """Creating goal"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)


class DiaryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryComment
        exclude = ['user']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)


class MentorCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorComment
        exclude = ['user']

    def create(self, validated_data):
        """Creating comment"""
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)
