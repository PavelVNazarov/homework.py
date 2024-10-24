# Домашнее задание по теме "Структура проекта. Маршруты и модели Pydantic."
# ННазаров ПВ
# module_17_1.py

from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
