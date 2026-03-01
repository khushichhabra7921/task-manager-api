# Task Manager API

A REST API for managing tasks with user authentication, built with FastAPI and Python.

## Features
- User registration and login with JWT authentication
- Full CRUD operations for tasks
- SQLite database with SQLAlchemy ORM
- Input validation with Pydantic
- Auto-generated API documentation
- 5 unit tests with pytest

## Tech Stack
Python, FastAPI, SQLAlchemy, SQLite, JWT, pytest

## Setup

1. Clone the repo
```
   git clone https://github.com/khushichhabra7921/task-manager-api.git
   cd task-manager-api
```

2. Create virtual environment
```
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```
   pip install -r requirements.txt
   pip install python-multipart
```

4. Run the server
```
   uvicorn main:app --reload
```

5. Open API docs at `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/register | Register a new user |
| POST | /users/login | Login and get JWT token |
| GET | /users/me | Get current user |
| POST | /tasks/ | Create a task |
| GET | /tasks/ | Get all tasks |
| GET | /tasks/{id} | Get a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Run Tests
```
pytest test_api.py -v
```
```

Save with Ctrl+S, then:
```
git add .
git commit -m "Add README"
git push
