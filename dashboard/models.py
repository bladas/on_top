import enum
import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class StatusEnum(enum.Enum):
    IN_PROGRESS = 'В процесі'
    DONE = 'Виконано'
    DECLINED = 'Відхилено'


class Goal(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[(tag.value, tag.value) for tag in StatusEnum],
                              default=StatusEnum.IN_PROGRESS.value)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class SubGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[(tag.value, tag.value) for tag in StatusEnum],
                              default=StatusEnum.IN_PROGRESS.value)
    description = models.TextField()


class SubGoalCompletion(models.Model):
    sub_goal = models.ForeignKey(SubGoal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class DiaryComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class MentorComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class GoalMentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class GoalReminding(models.Model):
    text = models.CharField(max_length=255)
    periodicity = models.CharField(max_length=255)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(default=datetime.time(16, 00))
