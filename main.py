from botStarter import Bot
bot = Bot("bot").get_bot()

# Define states for the conversation
user_data = {}

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! What's your name?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_data[message.chat.id] = {'name': message.text}
    bot.send_message(message.chat.id, "Thanks! What's your email?")
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    user_data[message.chat.id]['email'] = message.text
    bot.send_message(message.chat.id, "Great! How old are you?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    user_data[message.chat.id]['age'] = message.text
    data = user_data[message.chat.id]
    bot.send_message(
        message.chat.id,
        f"Here's the info you provided:\nName: {data['name']}\nEmail: {data['email']}\nAge: {data['age']}"
    )
    # Here you can save the data to a database if needed

# Optional: Cancel command or handle errors
@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "Form canceled.")
    if message.chat.id in user_data:
        del user_data[message.chat.id]
bot.infinity_polling()