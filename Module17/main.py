from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base
from app.models.task import Task
from app.models.user import User
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)

