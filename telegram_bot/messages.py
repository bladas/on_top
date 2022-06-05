from operator import itemgetter

from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ChosenInlineResult,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext

from dashboard.models import Goal
from telegram_bot.bot import bot
from telegram_bot.config import send_chunked_message
from telegram_bot.models import ButtonText, MessageText


def send_text_message(context: CallbackContext, user_id: int, text):
    message = bot.send_message(
        user_id,
        text=text,
    )

    context.chat_data["id"] = message.chat_id
    context.user_data["last_message_id"] = message.message_id


def send_contact_message(user_id: int, context) -> None:
    share_contact_button = KeyboardButton(
        ButtonText.objects.get(name="contact_button").text, request_contact=True
    )
    keyboard = ReplyKeyboardMarkup([[share_contact_button]])

    if "last_messages_ids" not in context.user_data:
        context.user_data["last_messages_ids"] = []

    message = bot.send_message(
        user_id,
        reply_markup=keyboard,
        text=MessageText.objects.get(name="contact_message").text,
    )
    context.user_data["last_messages_ids"].append(message.message_id)
    context.chat_data["id"] = message.chat_id


def send_otp_message(user_id, context, otp):
    message = bot.send_message(
        user_id,
        text=f"Використайте цей код для входу на сайт: {otp}",
    )

    context.chat_data["id"] = message.chat_id
    context.user_data["last_message_id"] = message.message_id


def get_list_of_goals_message(user_id, context):
    list_of_goals = KeyboardButton(
        "Отримати список цілей"
    )
    keyboard = ReplyKeyboardMarkup([[list_of_goals]])

    if "last_messages_ids" not in context.user_data:
        context.user_data["last_messages_ids"] = []

    message = bot.send_message(
        user_id,
        reply_markup=keyboard,
        text="Меню",
    )
    context.user_data["last_messages_ids"].append(message.message_id)
    context.chat_data["id"] = message.chat_id


def send_list_of_goals_message(user, context):
    goals = Goal.objects.filter(user=user)
    variant_buttons = [
        InlineKeyboardButton(
            goal.title,
            callback_data=str(goal.pk),
        )
        for goal in goals
    ]

    send_chunked_message(
        user_id=goals.chat_id,
        bot=bot,
        context=context,
        buttons=variant_buttons,
        chunk=1,
    )