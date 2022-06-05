from telegram_bot.bot import bot


def send_text_message(chat_id: str, text):
    bot.send_message(
        chat_id,
        text=text,
    )