import telebot
import config
from datetime import datetime, timedelta

bot = telebot.TeleBot(config.token)


def main():
    pass


@bot.message_handler(content_types=["poll"])
def poll_request():
    now = datetime.now()
    saturday = now - timedelta(days=now.weekday() - 5)
    sunday = now - timedelta(days=now.weekday() - 6)

    poll_msg = bot.send_poll(
        question=f"Работы на предстоящие выходные: {saturday.strftime('%d')} - {sunday.strftime('%d')} "
                 f"{datetime.now().strftime('%B')}",
        chat_id=-543395648,
        options=['пятница --> суббота', 'суббота', 'суббота --> воскресенье', 'воскресенье',
                 'не могу в эти выходные', 'превышен лимит по часам'],
        allows_multiple_answers=True,
        is_anonymous=False)
    bot.pin_chat_message(chat_id=-543395648, message_id=poll_msg.message_id)


if __name__ == '__main__':
    poll_request()
