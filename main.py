import telebot
import os
from flask import Flask, request
from news import *
from bs4 import BeautifulSoup
import requests
from googletrans import Translator

headers = {'User-agent': 'Mozilla/5.0'}

request = requests.get('https://www.skysports.com/football/news', headers=headers)
html = request.content

soup = BeautifulSoup(html, 'html.parser')

TOKEN = '5482902514:AAFawjggplZ2t87mthMLQj-uebJPTkpkAB4'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@server.route("/")
def football():
    news_list = []

    for h in soup.findAll(['a', 'p'], class_=['news-list__headline-link', 'news-list__snippet'], limit=10):
        news_title = h.contents[0].lower()

        if news_title not in news_list:
            if 'skysports' not in news_title:
                news_list.append(news_title)

    with open('out.txt', 'w', encoding='utf-8') as file:
        for i, title in enumerate(news_list):
            text = title.strip()
            translator = Translator()
            trans = translator.translate(text, dest='ru')
            res = i+1, trans.text
            
            tee = str(res)+'\n'
            file.write(tee.replace("(", "").replace(")","").replace("'","").replace(",","."))
    with open('out.txt', encoding='utf-8') as f:
        contents = f.read()      
        return contents, "!", 200

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/start':
        bot.reply_to(message, 'Привіт {name}'.format(name = message.chat.first_name))
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
