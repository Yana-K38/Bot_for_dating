import os

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

ABOUT_ME_MESSAGE = (
    "Рада с тобой познакомиться, {name}!\n"
    "Меня зовут Курзюкова Яна, я Python разработчик.\n"
    "Мои основные инструменты Python 3,6+, Django, "
    "так же я много работаю с API, PostgreSQL и др., "
    "знаю, что такое ООП и имею представление о шаблонах архитектуры, "
    "пишу запросы на SQL, "
    "упаковываю проекты в Docker, docker compose, Git.\n"
    "Активно изучаю FastAPI. Есть опыт работы в команде."
)

GITHUB_LINK = "https://github.com/Yana-K38/Bot_for_dating"


HELP_MESSAGE = (
    "Список доступных команд:\n"
    "/start - Начать диалог с ботом\n"
    "/about_me - Посмотреть информацию обо мне\n"
    "/question - Посмотреть список вопросов\n"
    "/my_github - Ссылка на мой GitHub репозиторий\n"
    "/exit, /cancel - Вернет в начало разговора"
)