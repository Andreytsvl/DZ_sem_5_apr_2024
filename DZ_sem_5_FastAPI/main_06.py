# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import logging
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [
    User(id=1, name="Aлиса", email="alice@example.com", password="12345kjhgu"),
    User(id=2, name="Борис", email="boris@example.com", password="ytrewq"),
]


@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
    logger.info(f'Обработан запрос для users')
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# if __name__ == "__main__":
#         uvicorn.run(app, host="127.0.0.1", port=8000)