import sqlite3
import datetime
import utils

weeknow = utils.weekcount()
weekday = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА']


def sort(str, week):
    temp = str.split(',')
    if temp.__len__() > 1:
        if week == 0:
            return temp[1]
    return temp[0]


class subjects:
    def __init__(self, database, day):
        self.day = day
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def get_today(self):
        with self.connection:
            dsch = self.cursor.execute('SELECT * FROM ' + self.day).fetchall()
            string = ''
            for d in dsch:
                string = string + d[0] + '-' + d[1] + ' : ' + sort(d[2], weeknow) + '\n'
            self.connection.commit()
            return string

    def get_tomorrow(self):
        with self.connection:
            dsch = self.cursor.execute(
                'SELECT * FROM ' + utils.daynow(datetime.datetime.weekday(datetime.datetime.now()) + 1)).fetchall()
            string = ''
            for d in dsch:
                string = string + d[0] + '-' + d[1] + ' : ' + sort(d[2], weeknow) + '\n'
            self.connection.commit()
            return string

    def get_week(self):
        with self.connection:
            string = ''
            for i in range(0, 6):
                string = string + '\n\n' + weekday[i] + '\n'
                dsch = self.cursor.execute(
                    'SELECT * FROM ' + utils.daynow(i)).fetchall()
                for d in dsch:
                    string = string + d[0] + '-' + d[1] + ' : ' + sort(d[2], weeknow) + '\n'
                self.connection.commit()
            return string

    def get_now(self):
        time = datetime.datetime.timetuple(datetime.datetime.now())
        with self.connection:
            time1 = []
            time2 = []
            dayly = self.cursor.execute('SELECT * FROM ' + self.day).fetchall()
            for d in dayly:
                time1.append(d[0])
                time2.append(d[1])
            for i in range(time1.__len__()):
                temp = time1[i].split(':')
                hh1 = int(temp[0])
                mm1 = int(temp[1])
                temp = time2[i].split(':')
                hh2 = int(temp[0])
                mm2 = int(temp[1])
                before = hh1 * 60 + mm1 - 10
                after = hh2 * 60 + mm2
                now = time.tm_hour * 60 + time.tm_min
                if before < now < after:
                    d = dayly[i]
                    self.connection.commit()
                    return sort(d[2], weeknow)
            return 'Сейчас занятий нет'

    def close(self):
        self.connection.close()