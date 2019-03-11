import config
import telebot
from SQLighter import subjects
import utils
import emoji


global schedule
schedule = subjects('schedule.db', utils.daynow())
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Привет! Я помогу тебе получать расписание!',
                     reply_markup=utils.menu_markup())

@bot.message_handler(content_types=['text'])
def text_reply(message):
    if message.text == emoji.emojize(':warning: Сейчас'):
        bot.send_message(message.chat.id, schedule.get_now())
    elif message.text == emoji.emojize(':eleven-thirty: Сегодня'):
        bot.send_message(message.chat.id, schedule.get_today())
    elif message.text == emoji.emojize(':fast-forward_button: Завтра'):
        bot.send_message(message.chat.id, schedule.get_tomorrow())
    elif message.text == emoji.emojize(':calendar: Неделя'):
        bot.send_message(message.chat.id, schedule.get_week())
    elif message.text == emoji.emojize(':question_mark: Справка'):
        bot.send_message(message.chat.id, utils.help())
    elif message.text == emoji.emojize(':warning: Сейчас'):
        bot.send_message(message.chat.id, schedule.get_now())

if __name__ == '__main__':
    bot.polling(none_stop=True)