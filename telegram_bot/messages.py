from datetime import datetime
from operator import itemgetter

from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ChosenInlineResult,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext

from dashboard.models import Goal, SubGoalCompletion, SubGoal
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
        if (SubGoal.objects.filter(goal=goal).first()
            and not SubGoalCompletion.objects.filter(sb_goal__goal=goal, created_at=datetime.now().date).first())
    ]
    if variant_buttons:
        text = "Виберіть ціль"
    else:
        text = "Всі цілі на сьогодні виконані!"
    send_chunked_message(
        user_id=user.chat_id,
        bot=bot,
        context=context,
        buttons=variant_buttons,
        text=text,
        chunk=1,
    )


def send_goal_approve_message(chat_id, goal_pk, context):
    goal = Goal.objects.get(pk=goal_pk)
    variant_buttons = [
        InlineKeyboardButton(
            "Виконано",
            callback_data=f"1, {goal_pk}",
        ),
        InlineKeyboardButton(
            "Не виконано",
            callback_data=f"0, {goal_pk}",
        ),

    ]
    sub_goals = SubGoal.objects.filter(goal=goal)
    titles = [sub_goal.title for sub_goal in sub_goals]
    text = "\n".join(titles)
    send_chunked_message(
        user_id=chat_id,
        bot=bot,
        context=context,
        buttons=variant_buttons,
        text=f"План на сьогодні виконаний?\n {text}",
        chunk=2,
    )


def comment_message(user_id, context, text):
    list_of_goals = KeyboardButton(
        "Отримати список цілей"
    )
    keyboard = ReplyKeyboardMarkup([[list_of_goals]])

    if "last_messages_ids" not in context.user_data:
        context.user_data["last_messages_ids"] = []

    message = bot.send_message(
        user_id,
        reply_markup=keyboard,
        text=text,
    )
    context.user_data["last_messages_ids"].append(message.message_id)
    context.chat_data["id"] = message.chat_id