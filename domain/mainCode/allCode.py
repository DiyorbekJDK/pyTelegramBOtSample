##################################
# Main code file, were bots work #
##################################

from domain.functions.botFunctions.botMainFunctions import *
from domain.functions.dbFunctions.databaseFunctions import *
from data.util.tokens import bot_token

bot = telebot.TeleBot(bot_token)


def allCode():
    @bot.message_handler(commands=['start'])
    def start(message):
        pass

    bot.polling(none_stop=True)
