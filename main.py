import telebot
token = "5785032666:AAHmweiukEUklqPhvcEjFw-q4IGZvJiehNU"

bot = telebot.TeleBot(token)

notes = {}

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == "/start":
        chat_id = message.chat.id
        answer = bot.send_message(message.chat.id, "Привет, сейчас я помогу тебе подобрать учебное заведение по вкусу.")
        bot.register_next_step_handler(answer, point1)
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="ВУЗ", callback_data="button1")
        button2 = telebot.types.InlineKeyboardButton(text="ПТУ", callback_data="button2")
        keyboard.row(button1, button2)
        bot.send_message(message.from_user.id, "Сделай выбор какое учебное заведение мне для тебя искать?", reply_markup=keyboard)



    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_function1(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()

    bot.send_message(callback_obj.from_user.id, "вы выбрали ВУЗ, введите ваши баллы ЕГЭ.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_function2(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()

    bot.send_message(callback_obj.from_user.id, "Вы  выбрали ПТУ, введите ваши баллы ОГЭ.", reply_markup=keyboard)


@bot.message_handler(commands=['remind'])
def remind(message):
    user.id = message.chat.id
    if user_id not in notes:
        bot.send_message(user_id, "Вы мне ещё ничего не писали.")
    else:
        bot.sed_message(user_id, notes[user_id])

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    notes[user_id] = message.text
    bot.send_message(user_id, "Я запомнил, спасибо.")


def point1(message):
    chat_id = message.chat.id
    text = message.text
    if text == "Ответ 1":
        answer = bot.send_message(chat_id, "Правильный ответ, второе задание...")
        bot.register_next_step_handler(answer, point2)

def point2(message):
    chat_id = message.chat.id
    text = message.text
    if text == "Ответ 2":
        answer = bot.send_message(chat_id, "Правильный ответ. Вы прошли квест!\nЧтобы повторить напишите /start.")
    else:
        answer = bot.send_message(chat_id, "Нет, попробуйте еще раз...")
        bot.register_next_step_handler(answer, point2)

bot.polling(none_stop=True)


bot.infinity_polling()
