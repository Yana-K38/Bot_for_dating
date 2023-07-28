from telebot import types

from config.config import ABOUT_ME_MESSAGE, GITHUB_LINK, HELP_MESSAGE


def hello_handler(bot, message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton(
        'Фото из старшей школы'), types.KeyboardButton('Последнее селфи'))
    keyboard.add(types.KeyboardButton('Мое увлечение'))
    welcome_text = (f"Привет, {message.from_user.first_name}!"
                    "Давай познакомимся поближе! Выбери, что тебе интересно:")
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     f"{message.from_user.first_name} "
                     "ты можешь посмотреть мои фотографии:")
    bot.send_message(message.chat.id,
                     "Для просмотра информации обо мне, напиши /about_me!")
    bot.send_message(message.chat.id,
                     "Для просмотра ответов на вопросы, напиши /question")
    bot.send_message(message.chat.id,
                     "Загляни на GitHub, там размещен публичный "
                     "репозиторий с исходниками этого бота /my_github")
    bot.send_message(message.chat.id,
                     "Ты можешь просмотреть список доступных команд /help")


def help_handler(bot, message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


def show_questions_handler(bot, message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Что такое чат GPT'),
                 types.KeyboardButton('Чем отличается SQL и NoSQL'),
                 types.KeyboardButton('История первой любви'))
    bot.send_message(message.chat.id, "Выбери вопрос из списка:", reply_markup=keyboard)


def about_me_handler(bot, message):
    about_me_message = ABOUT_ME_MESSAGE.format(name=message.from_user.first_name)
    bot.send_message(message.chat.id, about_me_message)


def my_github_handler(bot, message):
    bot.send_message(message.chat.id, GITHUB_LINK)


def exit_command_handler(bot, message):
    hello_handler(bot, message)


def unknown_command_handler(bot, message):
    known_commands = ['/start', '/help', '/question',
                      '/about_me', '/my_github', '/exit', '/cancel']
    known_menu_options = ['Фото из старшей школы', 'Последнее селфи',
                          'Мое увлечение', 'Что такое чат GPT',
                          'Чем отличается SQL и NoSQL', 'История первой любви']
    if message.text.startswith('/') and message.text not in known_commands:
        help_handler(bot, message)
    elif message.text in known_menu_options:
        menu_handler(bot, message)
    else:
        bot.reply_to(message, "Я не знаю такой команды. "
                              "Пожалуйста, воспользуйтесь /help"
                              "для получения списка доступных команд.")


def menu_handler(bot, message):
    if message.text == 'Фото из старшей школы':
        with open('media/photo/1.jpg', 'rb') as photo_file:
            bot.send_photo(message.chat.id, photo=photo_file,
                           caption='Фотографии больше 10 лет!')
    elif message.text == 'Последнее селфи':
        with open('media/photo/2.jpg', 'rb') as photo_file:
            bot.send_photo(message.chat.id, photo=photo_file,
                           caption='Мое последнее селфи из отпуска!')
    elif message.text == 'Мое увлечение':
        with open('media/text/Мое увлечение.txt', 'rb') as document_file:
            bot.send_document(message.chat.id, document=document_file)
    elif message.text == 'Что такое чат GPT':
        with open('media/voice/GPTchat.ogg', 'rb') as audioGPT:
            bot.send_audio(message.chat.id, audio=audioGPT)
    elif message.text == 'Чем отличается SQL и NoSQL':
        with open('media/voice/SQLvsNoSQL.ogg', 'rb') as audioSQLvsNoSQL:
            bot.send_audio(message.chat.id, audio=audioSQLvsNoSQL)
    elif message.text == 'История первой любви':
        with open('media/voice/love.ogg', 'rb') as audioLove:
            bot.send_audio(message.chat.id, audio=audioLove)
