# Домашнее задание по теме "Модели SQLALchemy. Отношения между таблицами."
# Назаров ПВ
# module_17_2.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем движок с использованием SQLite
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
