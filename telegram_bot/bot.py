from telegram import Bot
from django.conf import settings

bot = Bot(settings.TELEGRAM_BOT["TOKEN"])
bot.set_webhook(settings.TELEGRAM_BOT["WEBHOOK_URL"])
