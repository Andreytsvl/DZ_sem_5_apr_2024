# Задание №5
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из
# списка.
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


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user_index = None
    for index, user in enumerate(users):
        if user.id == user_id:
            user_index = index
            break
    if user_index is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
        logging.error(f'Ошибка 404. Пользователь не найден')
    deleted_user = users.pop(user_index)
    logger.info(f'Обработан Delete запрос для user')
    return deleted_user

if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)