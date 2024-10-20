from fastapi import FastAPI, HTTPException

app = FastAPI()

# Изначальная база данных пользователей
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    new_id = str(int(max(users.keys(), key=int)) + 1)  # Находим новый ID
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return f"User {user_id} has been deleted"

Пояснение к коду:
Импорт необходимых библиотек:

FastAPI и HTTPException для создания приложения и обработки ошибок.
Создание приложения:

Инициализация экземпляра FastAPI.
Изначальная база данных:

Словарь users, где ключ — это ID пользователя, а значение — строка с его данными.
GET запрос (/users):

Возвращает весь словарь users.
POST запрос (/user/{username}/{age}):

Добавляет нового пользователя. Находит максимальный ключ, увеличивает его на 1 и создает новую запись.
PUT запрос (/user/{user_id}/{username}/{age}):

Обновляет данные пользователя по его ID. Если пользователя нет, возвращает ошибку 404.
DELETE запрос (/user/{user_id}):

Удаляет пользователя по его ID. Если пользователя нет, возвращает ошибку 404.
Как проверить работу приложения:
Запустите сервер с помощью команды:

Bash
Копировать
uvicorn your_app_file_name:app --reload
Проверьте запрашиваемые пути:

GET /users
POST /user/UrbanUser/24
POST /user/NewUser/22
PUT /user/1/UrbanProfi/28
DELETE /user/2
GET /users
С помощью этого кода Вы сможете выполнять указанные CRUD операции с пользователями.
