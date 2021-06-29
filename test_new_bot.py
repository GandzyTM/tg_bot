import random
import nltk
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = '1670451566:AAHcknmZaLQmhMGSHCTxz_F0Nu9CTwz98ZE' # GandzyAIBot
updater = Updater(token, use_context=True)

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Добрый день', 'Приветик'],
            'responses': ['Привет человек', 'хаюшки']
        },
        'bye': {
            'examples': ['Пока', 'Покеда', 'Покусик'],
            'responses': ['Всего доброго', 'Покедос', 'и вам не хворать']
        },
        'emergency_phone_kids': {
            'examples': ['телефон детского врача', 'вызов детского врача', 'тел дет врача', 'детский врач',
                         'врач детский', 'вызвать детского врача'],
            'responses': [
                'https://yandex.ru/maps/org/otdeleniye_neotlozhnoy_meditsinskoy_pomoshchi/84870119492/?ll=60.607437%2C56.768851&z=17.55']
        },

    },
    'failure_phrases': [
        'Ваш запрос не понятен. Повторите.',
        'Повторите запрос.',
        'Возможно вы допустили ошибку в запросе. Повторите.'
    ]
}

def clear_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char in 'ёйцукенгшщзхъфывапролджэячсмитьбю')
    return text


def classify_intent(replica):
    replica = clear_text(replica)

    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            example = clear_text(example)

            distance = nltk.edit_distance(replica, example)
            if distance / len(example) < 0.3:
                return intent


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)


def generate_answer(replica):
    # TODO
    return


def get_stub():
    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)


def bot(replica):
    # NLU
    intent = classify_intent(replica)

    # get answer

    # rules
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer

    # generative model
    answer = generate_answer(replica)
    if answer:
        return answer

    # lock
    answer = get_stub()
    return answer


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Напишите интересующий вас вопрос.\n'
                                      'Например:\n'
                                      'Телефон охраны\n'
                                      'Вызов детского врача\n'
                                      'Детская поликлиника\n'
                                      'Взрослая поликлиника\n')

def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    message = bot(text)
    context.bot.send_message(chat_id=chat.id, text=message)
    # if text == 'privet':
    #     message = f'U send a {text}'
    #     context.bot.send_message(chat_id=chat.id, text=message)
    # else:
    #     context.bot.send_message(chat_id=chat.id, text="I can't understand U")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.text, on_message))

updater.start_polling()
updater.idle()