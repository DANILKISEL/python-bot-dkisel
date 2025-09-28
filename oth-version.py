import telebot

from botStarter import Bot
bot = Bot("bot").get_bot()


# Helper function to extract user_id from command argument or reply
def get_target_user_id(message):
    args = message.text.split()
    chat_id = message.chat.id

    if message.reply_to_message:
        # If replied, get user ID from replied message
        user_id = message.reply_to_message.from_user.id
        return user_id
    elif len(args) > 1:
        username = args[1]
        if username.startswith('@'):
            username = username[1:]
        try:
            # Resolve username to chat object
            chat_member = bot.get_chat(f"@{username}")
            return chat_member.id
        except Exception:
            bot.reply_to(message, "Could not find user with that username.")
            return None
    else:
        bot.reply_to(message, "Reply to a user's message or specify a username like /unban @username.")
        return None

@bot.message_handler(commands=['unban'])
def handle_unban(message):
    chat_id = message.chat.id
    user_id = get_target_user_id(message)
    if user_id is None:
        return
    try:
        bot.unban_chat_member(chat_id, user_id)
        bot.reply_to(message, "User has been unbanned.")
    except Exception:
        bot.reply_to(message, "Failed to unban user. Ensure I have the correct rights.")

@bot.message_handler(commands=['unmute'])
def handle_unmute(message):
    chat_id = message.chat.id
    user_id = get_target_user_id(message)
    if user_id is None:
        return
    try:
        # Remove restrictions (unmute)
        bot.restrict_chat_member(
            chat_id,
            user_id,
            permissions=telebot.types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
        )
        bot.reply_to(message, "User has been unmuted.")
    except Exception:
        bot.reply_to(message, "Failed to unmute user. Ensure I have the correct rights.")

# Run the bot
bot.polling()