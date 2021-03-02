import telebot

bot = telebot.TeleBot('993217806:AAHsXrVb3uRKX3P7R7Au5mYhJKueqEh0UxM')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Для использования бота напишите интересующий вас вопрос.\n'
                                      'Например:\n'
                                      'Телефон охраны')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'телефон охраны':
        bot.send_message(message.chat.id, '+79538241398')
    elif message.text.lower() == 'вызов детского врача':
        bot.send_message(message.chat.id, '+7(343)227-01-72')
    elif message.text.lower() == 'вызов врача':
        bot.send_message(message.chat.id, '')
    elif message.text.lower() == 'взрослая поликлиника':
        bot.send_message(message.chat.id, 'https://yandex.ru/maps/54/yekaterinburg/house/ulitsa_musorgskogo_2/YkkYcAZgQUwCQFtsfXt3cXthYw==/inside/?ll=60.611272%2C56.760478&z=17.71')



bot.polling()


def main():
    start_message()
    send_text()


if __name__ == "__main__":
    main()
