from datetime import datetime
import logging
from dashboard.models import GoalReminding
from on_top.celery import app
from telegram_bot.service import send_text_message


@app.task
def send_message():
    try:
        for reminding in GoalReminding.objects.filter(is_active=True):
            # if reminding.date.hour == datetime.now().hour:
            send_text_message(chat_id=reminding.user.chat_id, text=reminding.text)
    except:
        logging.warning("SENDING ERROR")
