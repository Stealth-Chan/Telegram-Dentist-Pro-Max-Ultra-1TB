from datetime import datetime
from time import *
import threading 
import telebot
import os

token = "write token here"
bot = telebot.TeleBot(token)

basadannuh = {}
last_book = [0]

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, "Hello, i am a bot that can help you with booking for dentist! you can use /reg command and book")

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id

@bot.message_handler(commands=['reg'])
def reg(message):
    user_id = message.from_user.id

    if not user_id in basadannuh and datetime.now().hour < 19 and last_book[0] < 20:
        if last_book[0] > datetime.now().hour:
            bot.send_message(user_id, f"You succesfully booked for dentist in {last_book[0]}:00 this day.")
            basadannuh[user_id] = {'name': message.from_user.first_name, "time": last_book[0]}
        else:
            last_book[0] = datetime.now().hour + 2
            bot.send_message(user_id, f"You succesfully booked for dentist in {last_book[0]}:00 this day.")
            basadannuh[user_id] = {'name': message.from_user.first_name, "time": last_book[0]}
    else:
        bot.send_message(user_id, "You're already booked or work day ended, try booking tommorow after 8.AM, waiting for you!")


@bot.message_handler(content_types=['text'])
def echo(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "I talk to you with commands, to check command list, type /help")

def log():
    sleep(60)
    os.system('cls')
    for client in basadannuh:
        name = client.name
        time = client.time
        print(f'Client {name} booked for time {time}:00\n\n')

os.system('cls')
threading.Thread(target=log).start()


