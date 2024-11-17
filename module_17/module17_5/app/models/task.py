from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter()


@router.get("/")
async def all_tasks(db: Session = Depends(get_db)):
    tasks = db.execute(select(Task)).scalars().all()
    return tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db_task = Task(**task.dict(), user_id=user_id, slug=slugify(task.title))
    db.add(db_task)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_task(task_id: int, task: UpdateTask, db: Session = Depends(get_db)):
    db_task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task.dict().items():
        setattr(db_task, key, value)

    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete("/delete")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.delete(db_task)
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'Task deleted successfully!'}


@router.get("/user/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    tasks = db.execute(select(Task).where(Task.user_id == user_id)).scalars().all()
    return tasks