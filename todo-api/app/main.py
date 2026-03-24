from fastapi import FastAPI, HTTPException
from app.models import Task, TaskCreate, TaskUpdate
from app.database import db

app = FastAPI(
    title="Todo API",
    description="A simple REST API to manage tasks",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to Todo API 🚀"}


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return db.get_all()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    return db.create(payload)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    task = db.update(task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if not db.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
