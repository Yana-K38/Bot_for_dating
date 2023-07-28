import telebot

from config.config import secret_token
from handlers import (about_me_handler, exit_command_handler, hello_handler,
                      help_handler, menu_handler, my_github_handler,
                      show_questions_handler, unknown_command_handler)

bot = telebot.TeleBot(token=secret_token)


@bot.message_handler(commands=['start'])
def on_start(message):
    hello_handler(bot, message)


@bot.message_handler(commands=['help'])
def on_help(message):
    help_handler(bot, message)


@bot.message_handler(commands=['question'])
def on_show_questions(message):
    show_questions_handler(bot, message)


@bot.message_handler(commands=['about_me'])
def on_aboutMe(message):
    about_me_handler(bot, message)


@bot.message_handler(commands=['my_github'])
def on_MyGithub(message):
    my_github_handler(bot, message)


@bot.message_handler(commands=['exit', 'cancel'])
def exit_command(message):
    exit_command_handler(bot, message)


@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    unknown_command_handler(bot, message)


@bot.message_handler(content_types=['text'])
def answer_for_questions(message):
    menu_handler(bot, message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
