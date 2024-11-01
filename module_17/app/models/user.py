# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# Назаров ПВ
# module_17_2.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db import Base  # Импортируем базовый класс


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

# @router.get("/")
# async def all_users():
#     pass
#
# @router.get("/{user_id}")
# async def user_by_id(user_id: int):
#     pass
#
# @router.post("/create")
# async def create_user():
#     pass
#
# @router.put("/update")
# async def update_user():
#     pass
#
# @router.delete("/delete")
# async def delete_user():
#     pass
def router():
    return None