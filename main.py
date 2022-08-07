import telebot
from newsbot import *

TOKEN = '5482902514:AAFawjggplZ2t87mthMLQj-uebJPTkpkAB4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'file'])
def main(message):
    if message.text == '/start':
        bot.reply_to(message, 'Привіт {name}'.format(name=message.from_user.first_name))
    elif message.text == '/news':    
        bot.reply_to(message, 'Йде обробка...')
        bot.send_message(message.from_user.id, football('football'))   
    else:
        bot.send_message(message.from_user.id, 'Будь-ласка, введіть команду /news')          
  
bot.polling(none_stop=True, interval=0)
