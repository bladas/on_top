from .bot import bot
# from .config import HOME_BUTTON, BACK_BUTTON
from .config import BACK_BUTTON
from .state import (
    CONTACT_STATE
)
from .handlers import (
    start_handler,
    contact_handler,
)

from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    Dispatcher,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    PicklePersistence,
    PreCheckoutQueryHandler,
)

dispatcher = Dispatcher(
    bot,
    workers=0,
    update_queue=None,
    persistence=PicklePersistence("telegram_bot/state"),
)

# Handle start command

start_command_handler = CommandHandler("start", start_handler)
# main_page_handler = MessageHandler(
#     Filters.regex(r"{}".format(HOME_BUTTON)),
#     main_page_handler,
# )
# back_button_dispatcher = MessageHandler(
#     Filters.regex(r"{}".format(BACK_BUTTON)),
#     back_button_handler,
# )
dispatcher.add_handler(
    ConversationHandler(
        name="main",
        persistent=True,
        entry_points=[CommandHandler("start", start_handler)],
        states={
            CONTACT_STATE: [
                start_command_handler,
                MessageHandler(filters=Filters.contact, callback=contact_handler),

            ],
        },
        fallbacks=[CommandHandler("start", start_handler)],

    )
)
