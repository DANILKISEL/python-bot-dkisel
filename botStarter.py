from telebot import TeleBot

class Bot:
    def __init__(self, botname):
        self.tokenFile = open("./token.txt", "r")
        self.token= self.tokenFile.read()
        self.defalutToken = "8472252626:AAEZnA6dXpxa-2NWoRuJ-S3FtiJxP9JqlAg"
        self.bot = TeleBot(self.defalutToken)
        self.botName = botname

    def get_bot(self):
        return self.bot