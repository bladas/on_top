from django.contrib.auth.models import AbstractUser
from django.db import models
from telegram import Contact

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
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField("email address", unique=True, blank=True, null=True)
    phone_number = models.CharField(
        max_length=16, validators=[validate_phone_number], unique=True, null=True, blank=True
    )
    chat_id = models.CharField(max_length=50, blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    @classmethod
    def init_from_contact(cls, contact: Contact):
        return cls(
            chat_id=contact.user_id,
            first_name=contact.first_name,
            last_name=contact.last_name or "None",
            phone_number=contact.phone_number,
        )