from django.db import models


# Create your models here.

class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
