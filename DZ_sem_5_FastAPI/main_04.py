# Задание №4
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
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


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    user_index = None
    for index, user in enumerate(users):
        if user.id == user_id:
            user_index = index
            break
    if user_index is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
        logging.error(f'Ошибка 404. Пользователь не найден')
    users[user_index] = user
    logger.info(f'Обработан Put запрос для user')
    return user


if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)