# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# ННазаров ПВ
# module_17_2.py

from routers.task import router as task_router
from routers.user import router as user_router
from fastapi import FastAPI
from models import Base
from backend.db import engine

app = FastAPI()

# Создаем все таблицы в базе данных
Base.metadata.create_all(bind=engine)

@app.get('/')
def read_root():
    return {"message": "Welcome to Taskmanager"}
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
