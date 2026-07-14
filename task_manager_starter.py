"""
Day Task: Mini FastAPI Task Manager
------------------------------------
Fill in each TODO below. Run locally with:
    uvicorn task_manager_starter:app --reload

Then open http://127.0.0.1:8000/docs to test your endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Mini Task Manager API")

# ---------------------------------------------------------
# SECTION 1: Data Model
# TODO: Define a Pydantic model called `Task` with fields:
#   - id: int
#   - title: str
#   - done: bool (default False)
# TODO: Define a second model `TaskUpdate` for partial updates
#   (title: Optional[str], done: Optional[bool])
# ---------------------------------------------------------


class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# ---------------------------------------------------------
# SECTION 2: In-memory storage
# TODO: Create a dictionary or list to hold tasks in memory.
# Example: tasks_db = {}
# ---------------------------------------------------------

tasks_db = {}


# ---------------------------------------------------------
# SECTION 3: Create Task
# TODO: Implement POST /tasks
#   - Accepts a Task object in the request body
#   - Stores it in tasks_db keyed by id
#   - Returns the created task
#   - If a task with that id already exists, raise HTTPException(400)
# ---------------------------------------------------------

@app.post("/tasks")
def create_task(task: Task):
    if task.id in tasks_db:
        raise HTTPException(status_code=400, detail="Task with this Id already exists")

    tasks_db[task.id] = task.model_dump()
    return task

# ---------------------------------------------------------
# SECTION 4: List Tasks
# TODO: Implement GET /tasks
#   - Returns all tasks currently stored
# ---------------------------------------------------------

@app.get("/tasks")
def list_tasks():
    return list(tasks_db.values())

# ---------------------------------------------------------
# SECTION 5: Get Single Task
# TODO: Implement GET /tasks/{task_id}
#   - Returns the task with that id
#   - If not found, raise HTTPException(404, detail="Task not found")
# ---------------------------------------------------------

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return tasks_db[task_id]

# ---------------------------------------------------------
# SECTION 6: Update Task
# TODO: Implement PUT /tasks/{task_id}
#   - Accepts a TaskUpdate object
#   - Updates only the fields provided
#   - If task doesn't exist, raise HTTPException(404)
#   - Return the updated task
# ---------------------------------------------------------

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task Not Found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    tasks_db[task_id].update(update_data)

    return tasks_db[task_id]


# ---------------------------------------------------------
# SECTION 7: Delete Task
# TODO: Implement DELETE /tasks/{task_id}
#   - Removes the task from tasks_db
#   - If task doesn't exist, raise HTTPException(404)
#   - Return a confirmation message
# ---------------------------------------------------------

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task Not Found")
    del tasks_db[task_id]
    return {"message": "Task deleted Successfully"}

# ---------------------------------------------------------
# SECTION 8: Self-check
# Once all endpoints are implemented, test each one manually
# via http://127.0.0.1:8000/docs before moving to Dockerization.
# ---------------------------------------------------------
