# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# Назаров ПВ
# module_17_2.py

from routers.task import router as task_router
from routers.user import router as user_router
from fastapi import FastAPI
from backend.db import engine, Base
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def read_root():
    return {"message": "Welcome to Taskmanager"}

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
