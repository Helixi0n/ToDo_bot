from telebot import TeleBot
from constants import TOKEN
from todo.controllers import Controller

bot = TeleBot(TOKEN)
controller = Controller(bot)

controller.register_handlers()

if __name__ == '__main__':
    print('Bot is running...')
    bot.polling()