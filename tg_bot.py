import telebot

bot = telebot.TeleBot('993217806:AAHsXrVb3uRKX3P7R7Au5mYhJKueqEh0UxM')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Для использования бота напишите интересующий вас вопрос.\n'
                                      'Например:\n'
                                      'Телефон охраны')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'телефон охраны':
        bot.send_message(message.chat.id, '+79538241398')
        bot.send_contact(message.chat.id, '+79538241398')


bot.polling()


def main():
    start_message()
    send_text()


if __name__ == "__main__":
    main()
