import telebot

bot = telebot.TeleBot('993217806:AAHsXrVb3uRKX3P7R7Au5mYhJKueqEh0UxM')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()


def main():
    start_message()
    send_text()


if __name__ == "__main__":
    main()
