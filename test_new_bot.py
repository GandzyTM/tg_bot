from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = '1670451566:AAHcknmZaLQmhMGSHCTxz_F0Nu9CTwz98ZE' # GandzyAIBot
updater = Updater(token, use_context=True)

BOT_CONFIG = {
    'intents': {
        'security_number': {
            'examples': ['тел охранника', 'тел охраны', 'телефон охранника', 'тел охраны'],
            'responses': ['+79538241398']
        },
        'emergency_number_kids': {
            'examples': ['вызов детского врача', 'детский врач', 'телефон вызова детского врача'],
            'responses': ['https://yandex.ru/maps/org/otdeleniye_neotlozhnoy_meditsinskoy_pomoshchi/84870119492/?ll=60.607437%2C56.768851&z=17.55', '+7(343)227-01-72']
        },
    },
    'failure_phrases': [
       'Не понятен ваш запрос',
       'Уточните запрос',
  ]
}

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
