from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class State(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="states"
    )
    num = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def set_state(self, user, state):
        self.user = user
        self.num = state
        self.save()

    @staticmethod
    def current_state(user):
        return State.objects.filter(user=user).order_by('-created_at')[0]

    @staticmethod
    def previous_state(user):
        return State.objects.filter(user=user).order_by('-created_at')[1]

    def __str__(self):
        return f'{self.user} {self.num}'


class MessageText(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.text}"


class ButtonText(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.text}"
