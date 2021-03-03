from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = '993217806:AAHsXrVb3uRKX3P7R7Au5mYhJKueqEh0UxM'
updater = Updater(token, use_context=True)

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Privet i'am bot")

def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    if text == 'privet':
        message = f'U send a {text}'
        context.bot.send_message(chat_id=chat.id, text=message)
    else:
        context.bot.send_message(chat_id=chat.id, text="I can't understand U")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
