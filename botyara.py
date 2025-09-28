from botStarter import Bot
bot = Bot("bot").get_bot()

from telebot import types

@bot.message_handler(commands=['game'])
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    itm1 = types.KeyboardButton("Камень")
    itm2 = types.KeyboardButton("Ножницы")
    itm3 = types.KeyboardButton("Бумага")
    markup.add(itm1, itm2, itm3)
    bot.send_message(message.chat.id, "Choose a game", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("/game")
    markup.add(button)
    bot.send_message(message.chat.id, "Hello! Lets start a game:", reply_markup=markup)
bot.infinity_polling()

