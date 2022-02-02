import asyncio

import telebot
from sqlalchemy.orm import Session

from dto.telegram_message_dto import MessageRequest
from repository import telegram_user_repository, telegram_message_repository

token = "bot token"
bot = telebot.TeleBot(token)


def send_message(message_request: MessageRequest, db: Session):
    if telegram_user_repository.is_username_exist(message_request.username, db):
        chat_id = telegram_user_repository.get_telegram_id_by_username(message_request.username, db)
        bot.send_message(chat_id=chat_id, text=message_request.text)
        return True
    else:
        return False


def get_messages(username: str, db: Session):
    user_id = telegram_user_repository.get_id_by_username(username, db)
    messages = telegram_message_repository.get_all_messages(user_id, db)
    return messages
