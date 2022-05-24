from django.contrib.auth.models import AbstractUser
from django.db import models


from .managers import CustomUserManager
from .validators import validate_phone_number


class CustomUser(AbstractUser):
    """
    Client stories:
        1. I want to sign in using Email and Password
        2. I want to create a new account indicating:
            1. First Name
            2. Last Name
            3. Company name
            4.  Phone number
            5. Email
            6. Password
        3. I want to reset my password
    """

    username = None
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField("email address", unique=True)
    phone_number = models.CharField(
        max_length=16, validators=[validate_phone_number], unique=True, null=True, blank=True
    )
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

