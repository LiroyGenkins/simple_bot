import telebot
from telebot import types
import psycopg2
from datetime import date

token = "[INPUT_TOKEN_HERE]"
bot = telebot.TeleBot(token)

connection = psycopg2.connect(user="postgres",
                              password="4245",
                              host="127.0.0.1",
                              port="5432",
                              database="raspisanie")
cursor = connection.cursor()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница","Суббота",
                 "Расписание на текущую неделю", "Расписание на следующую неделю")
    bot.send_message(message.chat.id,
                     'Здравствуйте! На какой день недели Вы хотите узнать расписание?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я умею выводить расписание для группы БТС1951 на выбранный день недели, а так же на текущю и следующую недели. Ещё я могу: \nпри использовании команды /mtuci дать ссылку на сайт МТУСИ, \nпри использовании команды /week вывести какая на данный момент неделя.')

@bot.message_handler(commands=['week'])
def start_message(message):
    current_date = date.today()
    begin = date(2022, 4, 4)
    delta = current_date - begin
    week = int(delta.days) // 7 if int(delta.days) % 7 == 0 else (int(delta.days) // 7) + 1
    bot.send_message(message.chat.id, f'Сейчас идёт {week} неделя семестра.')


@bot.message_handler(content_types=['text'])
def answer(message):
    ans = ""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    current_date = date.today()
    begin = date(2022, 4, 4)
    delta = current_date - begin
    week = int(delta.days) // 7 if int(delta.days) % 7 == 0 else (int(delta.days) // 7)
    if message.text.lower() == "понедельник":
        day = date(2022, 4, week * 7 + 4)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Понедельник' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Понедельник \n____________\n{ans}____________\n")
    elif message.text.lower() == "вторник":
        day = date(2022, 4, week * 7 + 5)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Вторник' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Вторник \n____________\n{ans}____________\n")
    elif message.text.lower() == "среда":
        day = date(2022, 4, week * 7 + 6)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Среда' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Среда \n____________\n{ans}____________\n")
    elif message.text.lower() == "четверг":
        day = date(2022, 4, week * 7 + 7)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Четверг' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Четверг \n____________\n{ans}____________\n")
    elif message.text.lower() == "пятница":
        day = date(2022, 4, week * 7 + 8)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Пятница' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Пятница \n____________\n{ans}____________\n")
    elif message.text.lower() == "суббота":
        day = date(2022, 4, week * 7 + 9)
        cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='Суббота' AND timetable.date='{day}';")
        record = cursor.fetchall()
        for i in record:
            for j in i:
                ans += j + "    "
            ans += "\n"
        bot.send_message(message.chat.id, f"Суббота \n____________\n{ans}____________\n")
    elif message.text.lower() == "расписание на текущую неделю":
        for i in range(4, 10):
            day = date(2022, 4, week * 7 + i)
            cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='{days[i-4]}' AND timetable.date='{day}';")
            record = cursor.fetchall()
            ans += f"{days[i-4]}\n____________\n"
            for i in record:
                for j in i:
                    ans += j + "    "
                ans += "\n"
            ans += "____________\n"
        bot.send_message(message.chat.id, f"Расписание на текущую неделю \n____________\n{ans}")
    elif message.text.lower() == "расписание на следующую неделю":
        ans = ""
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        for i in range(4, 10):
            day = date(2022, 4, (week + 1) * 7 + i)
            cursor.execute(f"SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.full_name FROM timetable RIGHT JOIN subject ON timetable.subject=subject.name RIGHT JOIN teacher ON subject.name=teacher.subject WHERE timetable.day='{days[i-4]}' AND timetable.date='{day}';")
            record = cursor.fetchall()
            ans += f"{days[i-4]}\n____________\n"
            for i in record:
                for j in i:
                    ans += j + "    "
                ans += "\n"
            ans += "____________\n"
        bot.send_message(message.chat.id, f"Расписание на следующую неделю \n____________\n{ans}")
    else:
        bot.send_message(message.chat.id, 'Извините, я Вас не понял')

bot.polling()


