from fastapi import FastAPI

from controller import telegram_controller

app = FastAPI()
app.include_router(telegram_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
