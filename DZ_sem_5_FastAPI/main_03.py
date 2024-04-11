# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

logging.basicConfig(filename='info.log.', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.post("/users/")
async def create_user(user: User):
    if user.id in [u.id for u in users]:
        raise HTTPException(status_code=400, detail="Пользователь с таким идентификатором уже существует")
        logging.error(f'Ошибка 400 Bad request. Пользователь уже существует ')
    users.append(user)
    logger.info(f'Обработан Post запрос для user')
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)