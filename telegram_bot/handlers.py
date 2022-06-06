import random

from django.contrib.auth import get_user_model
from telegram import Update, ReplyKeyboardRemove

from dashboard.models import DiaryComment
from .config import remove_last_message, data_dict
from .state import (
    CONTACT_STATE,
    HOME_STATE, GET_GOAL_STATE, APPROVE_STATE, COMENT_STATE
)
from .messages import *
from .models import MessageText, State

User = get_user_model()


def start_handler(update: Update, context) -> None:
    chat_id = update.message.from_user.id
    send_text_message(
        context=context,
        text=MessageText.objects.get(name="welcome").text,
        user_id=chat_id,
    )
    if User.objects.filter(chat_id=chat_id):
        keyboard_deleter = update.message.reply_text(
            "Секундочку...", reply_markup=ReplyKeyboardRemove()
        )
        keyboard_deleter.delete()
        get_list_of_goals_message(user_id=chat_id, context=context)
        state = State()
        state.set_state(User.objects.get(chat_id=chat_id), state=HOME_STATE)
        return HOME_STATE
    send_contact_message(user_id=chat_id, context=context)
    return CONTACT_STATE


def contact_handler(update: Update, context) -> None:
    remove_last_message(context)

    keyboard_deleter = update.message.reply_text(
        "Секундочку...", reply_markup=ReplyKeyboardRemove()
    )
    keyboard_deleter.delete()
    chat_id = update.message.from_user.id
    contact = update.effective_message.contact
    otp = random.randint(100000, 999999)
    user_data = {
        "phone_number": contact.phone_number,
        "password": str(otp),
        "last_name": contact.last_name or None,
        "first_name": contact.first_name,
        "chat_id": contact.user_id
    }
    user = User.objects.create_user(**user_data)
    state = State()
    state.set_state(user, state=HOME_STATE)
    send_otp_message(chat_id, context, otp)
    get_list_of_goals_message(chat_id, context)
    return HOME_STATE


def home_handler(update: Update, context) -> None:
    remove_last_message(context)
    chat_id = update.message.from_user.id
    user = User.objects.get(chat_id=chat_id)
    send_list_of_goals_message(user, context)
    state = State()
    state.set_state(user, state=GET_GOAL_STATE)
    return GET_GOAL_STATE


def goal_handler(update: Update, context) -> None:
    remove_last_message(context)
    user_id = update.callback_query.message.chat.id
    query = update.callback_query
    goal_pk = query["data"]
    send_goal_approve_message(user_id, goal_pk, context)
    user = User.objects.get(chat_id=user_id)
    state = State()
    state.set_state(user, state=APPROVE_STATE)
    return APPROVE_STATE


def approve_handler(update: Update, context) -> None:
    remove_last_message(context)
    user_id = update.callback_query.message.chat.id
    query = update.callback_query
    data = query["data"].split(',')
    if data[0] == "1":
        for sub_goal in SubGoal.objects.filter(goal__pk=data[1]):
            SubGoalCompletion.objects.create(
                sub_goal=SubGoal.objects.get(pk=sub_goal.pk)
            )
        data_dict['goal_pk'] = data[1]
    user = User.objects.get(chat_id=user_id)
    comment_message(context=context, user_id=user_id, text="Надішліть коментар до виконаого завдання,"
                                                             " або поверніться до списку цілей")

    state = State()
    state.set_state(user, state=COMENT_STATE)
    return COMENT_STATE


def comment_handler(update: Update, context) -> None:
    chat_id = update.message.from_user.id
    user = User.objects.get(chat_id=chat_id)
    DiaryComment.objects.create(
        user=user,
        goal=Goal.objects.get(pk=data_dict['goal_pk']),
        text=update.message.text
    )


