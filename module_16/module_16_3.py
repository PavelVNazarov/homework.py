# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Назаров ПВ
# module_16_3.py

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
