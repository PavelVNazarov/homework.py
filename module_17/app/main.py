# Домашнее задание по теме "Миграции. Библиотека alembic."
# Назаров ПВ
# module_17_3.py

from fastapi import FastAPI
from .backend.db import engine
#from .models import Base
from .backend.db import Base
app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
