import time
import telebot
token = "5785032666:AAHmweiukEUklqPhvcEjFw-q4IGZvJiehNU"
bot = telebot.TeleBot(token)

predmeties = {'Математика', 'математика','Физика', 'физика', 'Биология', 'биология', 'География', 'география', 'Немецкий язык', 'немецкий язык', 'Немецкий', 'немецкий', 'Русский язык', 'русский язык', 'Русский', 'русский', 'Английский язык', 'английский язык', 'Английский', 'английский', 'Литература', 'литература', 'Информатика', 'информатика', 'История', 'история', 'Химия', 'химия', 'Обществознание', 'обществознание', 'Китайский язык', 'китайский язык', 'Китайский', 'китайский'}

user_subjects = {}
user_points = {}


@bot.message_handler(commands=['start'])
def select_direction(message):
    bot.send_message(message.chat.id, "Привет, сейчас я помогу тебе подобрать учебное заведение по вкусу.")
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton(text="ВУЗ")
    button2 = telebot.types.KeyboardButton(text="ПТУ")
    keyboard.row(button1, button2)
    time.sleep(1)
    answer = bot.send_message(message.from_user.id, "Сделай выбор какое учебное заведение мне для тебя искать?",
                              reply_markup=keyboard)
    bot.register_next_step_handler(answer, direction_selected)


def direction_selected(message):
    direction = message.text

    if direction == "ВУЗ":
        answer = bot.send_message(message.from_user.id, "Вы выбрали ВУЗ, введите ваши баллы ЕГЭ.")
        bot.register_next_step_handler(answer, ege_points)
    elif direction == "ПТУ":
        answer = bot.send_message(message.from_user.id, "Вы  выбрали ПТУ, введите ваши баллы ОГЭ.")
        bot.register_next_step_handler(answer, oge_points)
    else:
        select_direction(message)


def ege_points(message):
    points = message.text

    if not points.isnumeric() or int(points) > 100 or int(points) < 0:
        answer = bot.send_message(message.from_user.id, "Введите число от 0 до 100.")
        bot.register_next_step_handler(answer, ege_points)
    else:
        user_points[message.chat.id] = int(points)
        superic = bot.send_message(message.from_user.id, "Какие предметы ты сдавал?")
        bot.register_next_step_handler(superic, predmety)

def oge_points(message):
    points1 = message.text

    if not points1.isnumeric() or int(points1) > 100 or int(points1) < 0:
        answer = bot.send_message(message.from_user.id, "Введите число от 0 до 100")
        bot.register_next_step_handler(answer, oge_points)
    else:
        user_points[message.chat.id] = int(points1)
        superic = bot.send_message(message.from_user.id, "Какие предметы ты сдавал?")
        bot.register_next_step_handler(superic, predmety1)

def predmety(message):
    subject = message.text

    if not subject != predmeties:
        superic = bot.send_message(message.from_user.id, "Введите предметы правильно. Например: "Математика"")
        bot.register_next_step_handler(superic, predmety)
    else:
        user_subjects[message.chat.id] = int(subject)


def predmety1(message):
    subject1 = message.text

    if not subject1 != predmeties:
        superic = bot.send_message(message.from_user.id, "Введите предметы правильно. Например: "Математика"")
        bot.register_next_step_handler(superic, predmety1)
    else:
        user_subjects[message.chat.id] = int(subject1)








bot.polling(none_stop=True)
