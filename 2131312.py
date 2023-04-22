#import sqlite3
import telebot
from collections import defaultdict

#conn = sqlite3.connect('example.db')
#import requests
#from bs4 import BeautifulSoup

#URL = "https://bmstu.ru/"
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "lxnl")
#post = soup.find("здесь атрибут", class_="здесь класс", id=True)
#post_id = post["id"]
#print(post_id)
#      илюша это переменные которые ты выводишь через бота
#balls = post.find("a", class_="").text.strip()
#location = post.find("div", class_="").text.strip()
#fak = post.find("a", class_="", href=True)["href"].strip()
#print(balls, location, fak)

#      Здесь начинаеться парсер
TOKEN = '5877376879:AAHpvNdGhFW7lRgg8AvT4OiTVSGWsdVogYM'

bot = telebot.TeleBot(TOKEN)

data = defaultdict(lambda: {"oge": None, "ege": None, "subj": None})


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, сейчас я помогу тебе подобрать учебное заведение по вкусу.")
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="ВУЗ", callback_data="button1")
        button2 = telebot.types.InlineKeyboardButton(text="ПТУ", callback_data="button2")
        keyboard.row(button1, button2)
        bot.send_message(message.from_user.id, "Сделай выбор: какое учебное заведение мне для тебя искать?",
                         reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Нажми /start для начала работы.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Нажми /help.")


@bot.callback_query_handler(func=lambda call: call.data in ["button1"])
def callback_function1(callback_obj):
    msg = bot.send_message(callback_obj.from_user.id, "Вы выбрали ВУЗ, пожалуйста введите баллы ЕГЭ.")
    bot.register_next_step_handler(msg, bally_ege)
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.callback_query_handler(func=lambda call: call.data in ["button2"])
def callback_function2(callback_obj):
    oop = bot.send_message(callback_obj.from_user.id, "Вы выбрали ПТУ, пожалуйста введите баллы ОГЭ")
    bot.register_next_step_handler(oop, bally_oge)
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.callback_query_handler(func=lambda call: call.data == "button100")
def bally_ege(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button27 = telebot.types.InlineKeyboardButton(text="Математика", callback_data="button27")
    button28 = telebot.types.InlineKeyboardButton(text="Физика", callback_data="button27")
    button29 = telebot.types.InlineKeyboardButton(text="Химия", callback_data="button27")
    button30 = telebot.types.InlineKeyboardButton(text="Биология", callback_data="button27")
    button31 = telebot.types.InlineKeyboardButton(text="География", callback_data="button27")
    button32 = telebot.types.InlineKeyboardButton(text="История", callback_data="button27")
    button33 = telebot.types.InlineKeyboardButton(text="Инофрматика", callback_data="button27")
    button34 = telebot.types.InlineKeyboardButton(text="Английский язык", callback_data="button27")
    button35 = telebot.types.InlineKeyboardButton(text="Литература", callback_data="button27")
    button36 = telebot.types.InlineKeyboardButton(text="Немецкий язык", callback_data="button27")
    button37 = telebot.types.InlineKeyboardButton(text="Обществознание", callback_data="button27")
    keyboard.row(button27, button28)
    keyboard.row(button29, button30)
    keyboard.row(button31, button32)
    keyboard.row(button33, button34)
    keyboard.row(button35, button36)
    keyboard.row(button37)
    if not message.text.isnumeric():
        m = bot.send_message(message.chat.id, "Это не число, введите число.")
        bot.register_next_step_handler(m, bally_ege)
        return

    if int(message.text) < 0 or int(message.text) > 300:
        m = bot.send_message(message.chat.id, "Введите число заново.")
        bot.register_next_step_handler(m, bally_ege)
        return

    data[message.chat.id].update({
        "ege": message.text,
    })
    jjj = bot.send_message(message.from_user.id, "Пожалуйста выберите предметы, которые вы сдавали.", reply_markup=keyboard)
    bot.register_next_step_handler(jjj, predmety1)


def bally_oge(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button38 = telebot.types.InlineKeyboardButton(text="Математика", callback_data="button38")
    button39 = telebot.types.InlineKeyboardButton(text="Физика", callback_data="button38")
    button40 = telebot.types.InlineKeyboardButton(text="Химия", callback_data="button38")
    button41 = telebot.types.InlineKeyboardButton(text="Биология", callback_data="button38")
    button42 = telebot.types.InlineKeyboardButton(text="География", callback_data="button38")
    button43 = telebot.types.InlineKeyboardButton(text="История", callback_data="button38")
    button44 = telebot.types.InlineKeyboardButton(text="Инофрматика", callback_data="button38")
    button45 = telebot.types.InlineKeyboardButton(text="Английский язык", callback_data="button38")
    button46 = telebot.types.InlineKeyboardButton(text="Литература", callback_data="button38")
    button47 = telebot.types.InlineKeyboardButton(text="Немецкий язык", callback_data="button38")
    button48 = telebot.types.InlineKeyboardButton(text="Обществознание", callback_data="button38")
    keyboard.row(button38, button39)
    keyboard.row(button40, button41)
    keyboard.row(button42, button43)
    keyboard.row(button44, button45)
    keyboard.row(button46, button47)
    keyboard.row(button48)
    if not message.text.isnumeric():
        s = bot.send_message(message.chat.id, "Это не число, введите число.")
        bot.register_next_step_handler(s, bally_oge)
        return

    if int(message.text) < 0 or int(message.text) > 342:
        s = bot.send_message(message.chat.id, "Введите число заново.")
        bot.register_next_step_handler(s, bally_oge)
        return

        data[message.chat.id].update({
        "oge": message.text,
    })
    jjj = bot.send_message(message.from_user.id, "Пожалуйста выберите предметы, которые вы сдавали.",
                           reply_markup=keyboard)
    bot.register_next_step_handler(jjj, predmety1)


@bot.callback_query_handler(func=lambda call: call.data == "button27")
def predmety1(message):
    bot.send_message(message.from_user.id,
                     "Самое подходящие для вас \n"                     "- [Наилучшее совпадение](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F50-srea)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "Второе наиболие подходящие для вас по отзывам\n"                     "- [этот тоже хорошо стоит присмотреться](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F312%2Fqpgc)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "И вот еще одно на которое мы бы вам посоветовали\n"                     "- [достойный вариант по нашему мнению](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F%3A6-srea)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "Если все три нижних не понравились есть это\n"                     "- [Если ничего не подошло то давайье сюда](https://example.com)",
                     parse_mode='MARKDOWN')

    data[message.chat.id].update({
        "subj": message.text, })


@bot.callback_query_handler(func=lambda call: call.data == "button38")
def predmety2(message):
    bot.send_message(message.from_user.id,
                     "Самое подходящие для вас \n"                     "- [Наилучшее совпадение](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F50-srea)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "Второе наиболие подходящие для вас по отзывам\n"                     "- [этот тоже хорошо стоит присмотреться](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F312%2Fqpgc)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "И вот еще одно на которое мы бы вам посоветовали\n"                     "- [достойный вариант по нашему мнению](https://proxy.geekclass.ru/service/hvtrs8%2F-pmsvuri%2Cilfm%2Faonlggg%2F%3A6-srea)",
                     parse_mode='MARKDOWN')
    bot.send_message(message.from_user.id,
                     "Если все три нижних не понравились есть это\n"                     "- [Если ничего не подошло то давайье сюда](https://example.com)",
                     parse_mode='MARKDOWN')
    data[message.chat.id].update({
        "subj": message.text,
    })

bot.infinity_polling()
