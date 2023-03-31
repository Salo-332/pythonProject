import sqlite3
import telebot
from collections import defaultdict

conn = sqlite3.connect('example.db')
import requests
from bs4 import BeautifulSoup

URL = "ссылка на сайт здесь"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
post = soup.find("здесь атрибут", class_="здесь класс", id=True)
post_id = post["id"]
print(post_id)
# илюша это переменные которые ты выводишь через бота
balls = post.find("a", class_="").text.strip()
location = post.find("div", class_="").text.strip()
fak = post.find("a", class_="", href=True)["href"].strip()
print(balls, location, fak)

# Здесь начинаеться парсер
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
        bot.send_message(message.from_user.id, "Сделай выбор какое учебное заведение мне для тебя искать?",
                         reply_markup=keyboard)

        # elif message.text == "/help":
        #     bot.send_message(message.from_user.id, "Напиши /start")
        # else:
        #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_function1(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button71 = telebot.types.InlineKeyboardButton(text="Программирование и информационные технологии",
                                                  callback_data="button71")
    button72 = telebot.types.InlineKeyboardButton(text="Медицинский", callback_data="button71")
    button73 = telebot.types.InlineKeyboardButton(text="Экономика и управление", callback_data="button71")
    button74 = telebot.types.InlineKeyboardButton(text="Строительство и энергетика", callback_data="button71")
    button75 = telebot.types.InlineKeyboardButton(text="Юриспруденция", callback_data="button71")
    button76 = telebot.types.InlineKeyboardButton(text="Реклама и СМИ", callback_data="button71")
    button77 = telebot.types.InlineKeyboardButton(text="Сервис и туризм", callback_data="button71")
    button78 = telebot.types.InlineKeyboardButton(text="Педагогика и психология", callback_data="button71")
    button79 = telebot.types.InlineKeyboardButton(text="Дизайн", callback_data="button71")
    button80 = telebot.types.InlineKeyboardButton(text="Анимация", callback_data="button80")
    button81 = telebot.types.InlineKeyboardButton(text="Актерское мастерство и искусство", callback_data="button81")
    button82 = telebot.types.InlineKeyboardButton(text="Лингвистика и переводоведение", callback_data="button82")
    keyboard.row(button71, button72, button73)
    keyboard.row(button74, button75, button76)
    keyboard.row(button77, button78, button79)
    keyboard.row(button80, button81, button82)
    bot.send_message(callback_obj.from_user.id, "вы выбрали факультет,теперь давайте введем баллы ЕГЭ",
                     reply_markup=keyboard)
    bot.register_next_step_handler(bally_ege)
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.callback_query_handler(func=lambda call: call.data == "button71")
def callback_function1(callback_obj):
    msg = bot.send_message(callback_obj.from_user.id, "Вы выбрали ВУЗ, пожалуйста введите баллы ЕГЭ")
    bot.register_next_step_handler(msg, bally_ege)
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_function2(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button21 = telebot.types.InlineKeyboardButton(text="Программирование и информационные технологии",
                                                  callback_data="button21")
    button22 = telebot.types.InlineKeyboardButton(text="Медицинский", callback_data="button22")
    button23 = telebot.types.InlineKeyboardButton(text="Экономика и управление", callback_data="button23")
    button24 = telebot.types.InlineKeyboardButton(text="Строительство и энергетика", callback_data="button24")
    button25 = telebot.types.InlineKeyboardButton(text="Юриспруденция", callback_data="button25")
    button26 = telebot.types.InlineKeyboardButton(text="Реклама и СМИ", callback_data="button26")
    button27 = telebot.types.InlineKeyboardButton(text="Сервис и туризм", callback_data="button27")
    button28 = telebot.types.InlineKeyboardButton(text="Педагогика и психология", callback_data="button28")
    button29 = telebot.types.InlineKeyboardButton(text="Дизайн", callback_data="button29")
    button30 = telebot.types.InlineKeyboardButton(text="Анимация", callback_data="button30")
    button31 = telebot.types.InlineKeyboardButton(text="Актерское мастерство и искусство", callback_data="button31")
    button32 = telebot.types.InlineKeyboardButton(text="Лингвистика и переводоведение", callback_data="button32")

    keyboard.row(button21, button22, button23)
    keyboard.row(button24, button25, button26)
    keyboard.row(button27, button28, button29)
    keyboard.row(button30, button31, button32)
    bot.send_message(callback_obj.from_user.id, "Вы  выбрали ПТУ, давайте выберем факультет", reply_markup=keyboard)
    psg = bot.send_message(callback_obj.from_user.id, "Вы выбрали ПТУ, пожалуйста введите ваши баллы ОГЭ ", )
    bot.register_next_step_handler(psg, bally_oge)
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.callback_query_handler(func=lambda call: call.data == "button100")
def bally_ege(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button2020 = telebot.types.InlineKeyboardButton(text="Математика", callback_data="button2020")
    button3 = telebot.types.InlineKeyboardButton(text="Физика", callback_data="button3")
    button4 = telebot.types.InlineKeyboardButton(text="Химия", callback_data="button4")
    button5 = telebot.types.InlineKeyboardButton(text="Биология", callback_data="button5")
    button6 = telebot.types.InlineKeyboardButton(text="География", callback_data="button5")
    button7 = telebot.types.InlineKeyboardButton(text="История", callback_data="button5")
    button8 = telebot.types.InlineKeyboardButton(text="Инофрматика", callback_data="button5")
    button9 = telebot.types.InlineKeyboardButton(text="Английский", callback_data="button5")
    button10 = telebot.types.InlineKeyboardButton(text="Литература", callback_data="button5")
    button11 = telebot.types.InlineKeyboardButton(text="Немецкий", callback_data="button5")
    button12 = telebot.types.InlineKeyboardButton(text="Обществознание", callback_data="button5")
    keyboard.row(button2020, button3)
    keyboard.row(button4, button5)
    keyboard.row(button6, button7)
    keyboard.row(button8, button9)
    keyboard.row(button10, button11)
    keyboard.row(button12)
    print(message.text)
    data[message.chat.id].update({
        "oge": message.text,
    })
    jjj = bot.send_message(message.from_user.id, "Пожалуйста выпишите из перечня предметы", reply_markup=keyboard)
    bot.register_next_step_handler(jjj, predmety1)


def bally_oge(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1001 = telebot.types.InlineKeyboardButton(text="Математика", callback_data="button1001")
    button1003 = telebot.types.InlineKeyboardButton(text="Физика", callback_data="button1003")
    button1004 = telebot.types.InlineKeyboardButton(text="Химия", callback_data="button1004")
    button1005 = telebot.types.InlineKeyboardButton(text="Биология", callback_data="button1005")
    button1006 = telebot.types.InlineKeyboardButton(text="География", callback_data="button1006")
    button1007 = telebot.types.InlineKeyboardButton(text="История", callback_data="button1007")
    button1008 = telebot.types.InlineKeyboardButton(text="Инофрматика", callback_data="button1008")
    button1009 = telebot.types.InlineKeyboardButton(text="Английский", callback_data="button1009")
    button1010 = telebot.types.InlineKeyboardButton(text="Литература", callback_data="button1010")
    button1011 = telebot.types.InlineKeyboardButton(text="Немецкий", callback_data="button1011")
    button1012 = telebot.types.InlineKeyboardButton(text="Обществознание", callback_data="button1012")
    keyboard.row(button1001, button1003)
    keyboard.row(button1004, button1005)
    keyboard.row(button1006, button1007)
    keyboard.row(button1008, button1009)
    keyboard.row(button1010, button1011)
    keyboard.row(button1012)
    print(message.text)
    data[message.chat.id].update({
        "oge": message.text,
    })
    jjj = bot.send_message(message.from_user.id, "Пожалуйста введите предметы, которые вы сдавали",
                           reply_markup=keyboard)
    bot.register_next_step_handler(jjj, predmety1)


@bot.callback_query_handler(func=lambda call: call.data == "button2020")
def predmety1(message):
    bot.send_message(message.from_user.id,
                     "Сейчас выдам список ВУЗОВ и подходящих вам профилей\n"                                           "- [Текст ссылки](https://example.com)",
                     parse_mode='MARKDOWN')

    data[message.chat.id].update({
        "subj": message.text,
    })


@bot.callback_query_handler(func=lambda call: call.data == "button100")
def predmety2(message):
    print(message.text)
    data[message.chat.id].update({
        "subj": message.text,
    })
    print(data)

    bot.send_message(message.from_user.id,
                     "Сейчас выдам список ПТУов и подходящих вам профилей\n"                     "- [Текст ссылки](https://example.com)",
                     parse_mode='MARKDOWN')


bot.infinity_polling()
