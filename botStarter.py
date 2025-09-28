import telebot

class Bot:
    def __init__(self, botname):
        self.tokenFile = open("token.txt", "r")
        self.token= self.tokenFile.read()
        self.bot = telebot.TeleBot(self.token)
        self.botName = botname

    def get_bot(self):
        return self.bot