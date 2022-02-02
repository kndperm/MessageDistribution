from pydantic import BaseModel


class MessageRequest(BaseModel):
    username: str
    text: str

    class Config:
        orm_mode = True
