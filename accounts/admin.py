from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserForm, CustomUserAddForm

# Register your models here.

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    add_form = CustomUserAddForm
    readonly_fields = [
        "is_staff",
        "is_active",
    ]
    list_display = (
        "id",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "phone_number",
    )
    list_filter = ("is_active", "is_phone_verified")
    fieldsets = (
        (
            "Authentication",
            {
                "fields": (
                    "phone_number",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",

                )
            },
        ),
        (
            "Statuses",
            {
                "fields": (
                    "is_phone_verified",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            "Authentication",
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Personal info",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                ),
            },
        ),
    )
    search_fields = (
        "phone_number",
        "first_name",
        "last_name",
    )
    ordering = ("id",)
