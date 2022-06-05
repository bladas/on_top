from django.contrib import admin
from .models import MessageText, ButtonText, State
# Register your models here.

admin.site.register(State)
admin.site.register(MessageText)
admin.site.register(ButtonText)

