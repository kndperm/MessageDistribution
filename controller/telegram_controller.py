from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dto import telegram_message_dto
from model.database import SessionLocal
from service import telegram_service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/telegram/post/", tags=["telegram"])
async def post_telegram_message(message: telegram_message_dto.MessageRequest, db: Session = Depends(get_db)):
    result = telegram_service.send_message(message, db)
    return {"isSend": result}


@router.get("/telegram/get/", tags=["telegram"])
async def get_telegram_messages(username: str, db: Session = Depends(get_db)):
    result = telegram_service.get_messages(username, db)
    return {"messsages": result}
