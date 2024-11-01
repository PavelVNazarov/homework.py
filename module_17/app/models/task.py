# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# Назаров ПВ
# module_17_2.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base  # Импортируем базовый класс


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')

# @router.get("/")
# async def all_tasks():
#     pass
#
# @router.get("/{task_id}")
# async def task_by_id(task_id: int):
#     pass
#
# @router.post("/create")
# async def create_task():
#     pass
#
# @router.put("/update")
# async def update_task():
#     pass
#
# @router.delete("/delete")
# async def delete_task():
#     pass
def router():
    return None