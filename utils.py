from telebot import types
import config
import datetime


def help():
    return 'Бот учитывает чётные/нечётные недели в расписании.\nСейчас - узнать, занятие по какому предмету проходит в данный момент\nСегодня - расписание на сегодня\nЗавтра - расписание на завтра\nНеделя - расписание на неделю'

def menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for item in config.menu_keyboard.split(','):
        buttons.append(types.KeyboardButton(item))
    markup.row(buttons[5])
    markup.row(buttons[0], buttons[1], buttons[2])
    markup.row(buttons[3], buttons[4])
    return markup

def daynow(date = datetime.datetime.weekday(datetime.datetime.now())):
    return {
        0: 'monday',
        1: 'tuesday',
        2: 'wednesday',
        3: 'thursday',
        4: 'friday',
        5: 'saturday',
        6: 'sunday'
    }[date]

def weekcount():
    delta = datetime.datetime.now() - datetime.datetime(2018, 9, 1)
    return ((delta.days - (7 - datetime.datetime.weekday(datetime.datetime(2018, 9, 1))))//7)%2