from fastapi import FastAPI
from database import engine
import models
from routes import users, tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A REST API for managing tasks with user authentication",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager API", "docs": "/docs"}

    # testing AI review