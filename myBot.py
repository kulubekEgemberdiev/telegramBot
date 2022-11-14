import telebot
from telebot import types


bot = telebot.TeleBot()


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f"🖐 Привет, {msg.from_user.full_name}! Чтобы получить список команд нажмите '/help'")


@bot.message_handler(content_types=['document'])
def get_user_docs(msg):
    bot.send_message(msg.chat.id, "Я обязательно прочитаю твой документ 🤥!")


@bot.message_handler(content_types=['audio'])
def get_user_audio(msg):
    bot.send_message(msg.chat.id, f"Отличная музыка, {msg.from_user.first_name}!")


@bot.message_handler(content_types=['voice'])
def get_user_voice(msg):
    bot.send_message(msg.chat.id, f"Прослушаю твое голосовое сообщение, когда у меня будет свободная минутка.")


@bot.message_handler(commands=['opengroup'])
def tg_group(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти', url="https://t.me/pyproglib"))
    bot.send_message(message.chat.id, "Перейти в группу", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton("/start")
    opengroup = types.KeyboardButton("/opengroup")
    markup.add(start, opengroup)
    bot.send_message(msg.chat.id, "Кнопки 👇", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(msg):
    bot.send_message(msg.chat.id, "Я вас не понял! Чтобы получить список команд нажмите '/help'")


bot.polling(none_stop=True)