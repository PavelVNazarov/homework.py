# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# ННазаров ПВ
# module_17_2.py

from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
