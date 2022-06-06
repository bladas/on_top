from telegram import Bot
from django.conf import settings


bot = Bot(settings.WRITER_BOT["TOKEN"])
if bot.getWebhookInfo().url != settings.WRITER_BOT["WEBHOOK_URL"]:
    bot.set_webhook(settings.WRITER_BOT["WEBHOOK_URL"])
