import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

tokenFile = open("token.txt", "r")
token = tokenFile.read()
bot = telebot.TeleBot(token)


# Welcome new members
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        bot.send_message(
            message.chat.id,
            f"🎉 Welcome, {new_member.first_name}! Please read the group rules and enjoy your stay."
        )

# Handle commands like /help and /info
@bot.message_handler(commands=['help'])
def handle_help(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("Group Rules", callback_data='rules'),
        InlineKeyboardButton("Bot Info", callback_data='info')
    )
    keyboard.row(
        InlineKeyboardButton("Contact Support", url='https://t.me/DkiselDK')
    )
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)

# Ban a user via reply with /ban
@bot.message_handler(commands=['ban'])
def handle_ban(message):
    if message.reply_to_message:
        user_to_ban = message.reply_to_message.from_user
        try:
            bot.kick_chat_member(message.chat.id, user_to_ban.id)
            bot.reply_to(message, f"User {user_to_ban.first_name} has been banned.")
        except Exception as e:
            bot.reply_to(message, "Failed to ban user. Make sure I have admin rights and try again.")
    else:
        bot.reply_to(message, "Reply to a user's message with /ban to ban them.")

# Inline callback handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'rules':
        bot.answer_callback_query(call.id, "Group Rules:\n1. Be respectful\n2. No spam\n3. Follow the Telegram Terms.")
    elif call.data == 'info':
        bot.answer_callback_query(call.id, "I'm a helpful group assistant bot.")

bot.polling()