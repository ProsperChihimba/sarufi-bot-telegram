import time
import telegram
import logging
from app import respond
from telegram import Update
from telegram.ext import (
    CommandHandler,
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
)

updater = Updater("5553349289:AAHHQjUh34sA3aN259rxeJi-Yq7f3h42kGQ", use_context=True)
mybot = updater.dispatcher

# initialize the logger
logger = logging.getLogger()


def simulate_typing(update: Update, context: CallbackContext):
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING
    )
    time.sleep(0.5)


def reply_with_typing(update: Update, context: CallbackContext, message):
    simulate_typing(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def start(update: Update, context: CallbackContext):
    """
    Starts the bot.
    """
    first_name = update.message.chat.first_name
    reply_with_typing(
        update,
        context,
        f"Hi {first_name}!\n Mimi no Robot naweza kukusaidia kununua bidhaa kwa urahisi.",
    )


def help(update: Update, context: CallbackContext):
    """
    Shows the help message.
    """
    reply_with_typing(update, context, "Help message")


def echo(update: Update, context: CallbackContext):
    """
    Echoes the user's message.
    """
    chat_id = update.message.chat.id
    response = respond(update.message.text, chat_id)
    reply_with_typing(update, context, response)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


mybot.add_handler(CommandHandler("start", start))
mybot.add_handler(CommandHandler("help", help))
mybot.add_handler(MessageHandler(Filters.text, echo))
mybot.add_error_handler(error)

if __name__ == "__main__":
    print("Starting bot...")
    updater.start_polling()