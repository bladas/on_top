import re

from django.core.exceptions import ValidationError

phone_number_regex = re.compile(r"^\+?\d{9,15}$")


def validate_phone_number(phone_number):
    """
    Phone_number must have up to 15 digits"
    """
    if phone_number_regex.match(phone_number) is None:
        raise ValidationError(
            "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
