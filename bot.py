import os
import time

from dotenv import load_dotenv
import telebot

from settings import TELEGRAM_TOKEN
import weather


bot = telebot.TeleBot(TELEGRAM_TOKEN)

get_weather_flag = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Сообщение бота')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global get_weather_flag
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Отправь геопозицию')
        get_weather_flag = True
    else:
        bot.send_message(message.chat.id, message.text)
    
    for key, value in message.json.items():
        if key == 'date':
            print(time.ctime(int(value)))
        print(f'{key}: {value}')

@bot.message_handler(content_types=['location'])
def get_location(message):
    global get_weather_flag
    if get_weather_flag:
        get_weather_flag = False
        loc_weather = weather.get_weather(message.location.latitude, message.location.longitude)
        if weather != -1:
            text = (
                f"За окном {loc_weather['weather'][0]['description']}, "
                f"температура {loc_weather['main']['temp']} "
                f"ощущается как {loc_weather['main']['feels_like']}"
            )
            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, 'Нет связи с сервером погоды')

if __name__ == "__main__":
    bot.polling()
