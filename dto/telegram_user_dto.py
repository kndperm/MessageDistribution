from pydantic import BaseModel


class TelegramUserCreate(BaseModel):
    username: str
    telegram_id: str

    class Config:
        orm_mode = True
