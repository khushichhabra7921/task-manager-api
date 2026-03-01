from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base, get_db

# Use a separate test database
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "email": "pytest@example.com",
        "username": "pytestuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "pytest@example.com"

def test_register_duplicate_user():
    client.post("/users/register", json={
        "email": "dupe@example.com",
        "username": "dupeuser",
        "password": "testpass123"
    })
    response = client.post("/users/register", json={
        "email": "dupe@example.com",
        "username": "dupeuser",
        "password": "testpass123"
    })
    assert response.status_code == 400

def test_login_user():
    client.post("/users/register", json={
        "email": "login@example.com",
        "username": "loginuser",
        "password": "testpass123"
    })
    response = client.post("/users/login", data={
        "username": "loginuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task():
    client.post("/users/register", json={
        "email": "task@example.com",
        "username": "taskuser",
        "password": "testpass123"
    })
    login = client.post("/users/login", data={
        "username": "taskuser",
        "password": "testpass123"
    })
    token = login.json()["access_token"]
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "This is a test",
        "status": "todo"
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    client.post("/users/register", json={
        "email": "gettask@example.com",
        "username": "gettaskuser",
        "password": "testpass123"
    })
    login = client.post("/users/login", data={
        "username": "gettaskuser",
        "password": "testpass123"
    })
    token = login.json()["access_token"]
    response = client.get("/tasks/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
