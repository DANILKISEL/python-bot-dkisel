import random
from botStarter import Bot
from telebot import types

bot = Bot("bot").get_bot()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("/game")
    markup.add(button)
    bot.send_message(message.chat.id, "Hello! Let's start a game:", reply_markup=markup)

@bot.message_handler(commands=['game'])
def game(message):
    markup = types.InlineKeyboardMarkup(row_width=3)

    # Use inline buttons with callback_data matching English options
    itm1 = types.InlineKeyboardButton(text="Камень", callback_data="Rock")
    itm2 = types.InlineKeyboardButton(text="Ножницы", callback_data="Scissors")
    itm3 = types.InlineKeyboardButton(text="Бумага", callback_data="Paper")
    markup.add(itm1, itm2, itm3)

    bot.send_message(message.chat.id, "Choose a move:", reply_markup=markup)

answer_pool = ["Rock", "Paper", "Scissors"]

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot_answer = random.choice(answer_pool)
    user_choice = call.data

    # Send bot's move to user
    bot.send_message(call.message.chat.id, f"Bot chooses: {bot_answer}")

    # Determine result
    result = (answer_pool.index(user_choice) - answer_pool.index(bot_answer)) % 3

    if result == 1:
        message = "YOU WIN"
    elif result == 2:
        message = "YOU LOSE"
    else:
        message = "TIE"

    bot.send_message(call.message.chat.id, message)

bot.infinity_polling()