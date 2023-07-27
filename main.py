import telebot
from telebot import types
import os

from dotenv import load_dotenv 

load_dotenv()

secret_token = os.getenv('TOKEN')

bot = telebot.TeleBot(token=secret_token)

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Фото из старшей школы'), types.KeyboardButton('Последнее селфи'))
    keyboard.add(types.KeyboardButton('Мое увлечение'))
    
    welcome_text = f"Привет, {message.from_user.first_name}! Давай познакомимся поближе! Выбери, что тебе интересно:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Фото из старшей школы':
        with open('1.jpg', 'rb') as photo_file:
            bot.send_photo(message.chat.id, photo=photo_file, caption='Фотографии больше 10 лет!')
    elif message.text == 'Последнее селфи':
        with open('2.jpg', 'rb') as photo_file:
            bot.send_photo(message.chat.id, photo=photo_file, caption='Мое последнее селфи из отпуска!')
    elif message.text == 'Мое увлечение':
        with open('Мое увлечение.txt', 'rb') as document_file:
            bot.send_document(message.chat.id, document=document_file)

bot.polling(none_stop=True)