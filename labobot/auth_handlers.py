from telebot.apihelper import ApiTelegramException
from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.types import Message

from labobot.configuration import bot

import database.main_db.common_crud as common_crud
from database.main_db.common_crud import UserEnum


class AuthStates(StatesGroup):
    full_name = State()


async def is_subscribed(chat_id: int, user_id: int) -> bool:
    try:
        response = await bot.get_chat_member(chat_id, user_id)
        if response.status == 'left':
            return False
        else:
            return True
    except ApiTelegramException as ex:
        if ex.result_json['description'] == 'Bad Request: user not found':
            return False


@bot.message_handler(commands=['start'])
async def handle_start(message: Message):
    user = common_crud.user_verification(message.from_user.id)
    match user:
        case UserEnum.Admin:
            await bot.send_message(
                message.chat.id,
                '<b>Привет, о могущественный админ! 😎 Попрошу вас не нажимать на красные кнопки случайно.🔴</b>',
                parse_mode='HTML',
                # TODO: клавиатура
            )
        case UserEnum.Teacher:
            await bot.send_message(
                message.chat.id,
                '<b>Приветствую учитель! 📚✨ Я помогу вам  сделать учебный процесс продуктивнее и увлекательнее!</b>',
                parse_mode='HTML',
                # TODO: клавиатура
            )
        case UserEnum.Student:
            await bot.send_message(
                message.chat.id,
                '<b>Привет! 🌟🎓 Рады видеть тебя здесь! Давай вместе сделаем этот учебный путь интересным и результативным</b>!',
                parse_mode='HTML',
                # TODO: клавиатура
            )
        case _:
            await bot.send_message(
                message.chat.id,
                '<b>Приветствие, о загадочный пользователь! 🤔🔍 Давайте попробуем разгадать эту загадку вместе!</b>',
                parse_mode='HTML',
                # TODO: клавиатура
            )