import telebot
from news import *
bot = telebot.TeleBot('5482902514:AAHh8wa03HfH3XY7T8FrcYEoD-c0EjUGY14')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привіт, надсилай свої ідеї чи контент") 
    elif message.text == '/news':
        bot.send_message(message.from_user.id, "Йде обробка... ") 
        bot.send_message(message.from_user.id, football('football')) 
    elif message.content_type == 'photo':  
        img = message.photo[2].file_id
        bot.send_message(986817461, "Запит від @{name} десь там 👇".format(name=message.chat.username), parse_mode="Markdown")
        bot.send_photo(986817461, img, message.caption)
        bot.reply_to(message, "Дякую *{name}* за співпрацю! Контент відправлено на огляд.".format(name=message.chat.first_name, text=message.text), parse_mode="Markdown")    
    else:
        bot.send_message(986817461, "Запит від @{name} десь там 👇".format(name=message.chat.username), parse_mode="Markdown")
        bot.send_message(986817461, message.text)
        bot.reply_to(message, "Дякую *{name}* за співпрацю! Контент відправлено на огляд.".format(name=message.chat.first_name, text=message.text), parse_mode="Markdown")   
          

bot.polling(none_stop=True, interval=0)