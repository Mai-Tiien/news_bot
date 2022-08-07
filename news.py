import telebot
import os
from flask import Flask, request
from news import *

TOKEN = '5482902514:AAFawjggplZ2t87mthMLQj-uebJPTkpkAB4'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/start':
        bot.reply_to(message, 'Привіт')
    elif message.text == '/news':
        bot.reply_to(message, 'Йде обробка...')
        bot.send_message(message.from_user.id, football('football'))   
    else:
        bot.send_message(message.from_user.id, 'Будь-ласка, введіть команду /news')
           

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://newsfootballduet-bot.herokuapp.com/' + TOKEN)
    return "!", 200           
  
if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8443))) 
