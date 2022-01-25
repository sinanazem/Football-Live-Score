import os

import telebot
from loguru import logger

telegram_bot_token = os.environ['TELEGRAMBOT_TOKEN']

class Bot():

    def __init__(self):
        self.bot = telebot.TeleBot(telegram_bot_token)
        logger.info("start bot...")
    def run(self):

        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?",reply_markup=create_keybord('Bitcoin'))



        self.bot.infinity_polling()

if __name__ == "__main__":
    obj = Bot()
    obj.run()
    print("Done!")
