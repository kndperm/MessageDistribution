from sqlalchemy.orm import Session

from model.telegram_model import TelegramMessage


def get_all_messages(user_id: int, db: Session):
    return db.query(TelegramMessage).filter(TelegramMessage.user_id == user_id).all()
