# Day Task: FastAPI Task Manager + Dockerization

## Goal
Complete the TODOs in `task_manager_starter.py` to build a working REST API,
then containerize it using the `Dockerfile` provided.

## Part 1 — FastAPI (fill in the TODOs)
Work through `task_manager_starter.py` top to bottom:
1. Define the `Task` and `TaskUpdate` Pydantic models
2. Set up in-memory storage
3. Implement `POST /tasks`
4. Implement `GET /tasks`
5. Implement `GET /tasks/{task_id}`
6. Implement `PUT /tasks/{task_id}`
7. Implement `DELETE /tasks/{task_id}`

Test locally:
```bash
pip install -r requirements.txt
uvicorn task_manager_starter:app --reload
```
Open http://127.0.0.1:8000/docs and test every endpoint.

## Part 2 — Dockerize (fill in the TODOs)
Work through the `Dockerfile` TODOs, then:
```bash
docker build -t task-api .
docker run -p 8000:8000 task-api
```
Confirm http://127.0.0.1:8000/docs still works from the container.

## Deliverables (submit by end of day)
1. Completed `task_manager_starter.py`
2. Completed `Dockerfile`
3. Screenshot of Swagger UI (`/docs`) showing all 5 endpoints working
4. Short write-up (3–5 sentences): what you learned, what was confusing,
   one thing you'd improve

## Optional (if time allows)
- Add a `docker-compose.yml`
- Push your image to Docker Hub and share the link
