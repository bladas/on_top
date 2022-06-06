from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from telegram_bot.service import send_text_message
from .models import GoalReminding


@receiver(post_save, sender=GoalReminding)
def my_handler(sender, **kwargs):
    for reminding in GoalReminding.objects.filter(is_active=True):
        if reminding.date.hour == datetime.now().hour:
            send_text_message(chat_id=reminding.user.chat_id, text=reminding.text)
