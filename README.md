# AI-Powered Task Manager API

A production-ready REST API for managing tasks with AI-powered prioritization, built with FastAPI and Python.

## 🚀 Live API
**Base URL:** https://task-manager-api-taq2.onrender.com  
**Interactive Docs:** https://task-manager-api-taq2.onrender.com/docs

## ✨ Features
- User registration and login with JWT authentication
- Full CRUD operations for tasks (Create, Read, Update, Delete)
- **AI-powered task prioritization** using Groq LLM (Llama 3.3) — analyzes deadlines and status to suggest optimal work order
- Pagination and filtering (`?page=1&limit=10&status=todo`)
- SQLite database with SQLAlchemy ORM
- Input validation with Pydantic
- Dockerized for one-command deployment
- GitHub Actions CI/CD pipeline (auto-runs tests on every push)
- 5 unit tests with pytest
- Auto-generated interactive API documentation (Swagger UI)

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| Python 3.13 | Core language |
| FastAPI | Web framework |
| SQLAlchemy | ORM / Database |
| SQLite | Database |
| JWT (python-jose) | Authentication |
| Pydantic | Data validation |
| Groq LLM (Llama 3.3) | AI task prioritization |
| Docker | Containerization |
| GitHub Actions | CI/CD Pipeline |
| pytest | Unit testing |
| Render | Cloud deployment |

## 📁 Project Structure
```
task-manager-api/
├── main.py                  # App entry point
├── database.py              # Database connection
├── models.py                # SQLAlchemy models
├── schemas.py               # Pydantic schemas
├── auth.py                  # JWT authentication
├── ai.py                    # Groq LLM integration
├── routes/
│   ├── users.py             # User endpoints
│   └── tasks.py             # Task + AI endpoints
├── test_api.py              # Unit tests
├── Dockerfile               # Docker image
├── docker-compose.yml       # Docker compose
├── requirements.txt         # Dependencies
└── .github/
    └── workflows/
        └── ci.yml           # GitHub Actions CI
```

## ⚙️ Local Setup

1. **Clone the repo**
```bash
   git clone https://github.com/khushichhabra7921/task-manager-api.git
   cd task-manager-api
```

2. **Create and activate virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set environment variables**
```bash
   $env:GROQ_API_KEY="your-groq-api-key"       # Windows
   export GROQ_API_KEY="your-groq-api-key"      # Mac/Linux
```

5. **Run the server**
```bash
   uvicorn main:app --reload
```

6. **Open API docs**
```
   http://127.0.0.1:8000/docs
```

## 🐳 Run with Docker
```bash
docker-compose up --build
```
No Python installation needed — just Docker.

## 🧪 Run Tests
```bash
pytest test_api.py -v
```

## 📡 API Endpoints

### Auth
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/users/register` | Register a new user | No |
| POST | `/users/login` | Login and get JWT token | No |
| GET | `/users/me` | Get current user profile | Yes |

### Tasks
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/tasks/` | Create a new task | Yes |
| GET | `/tasks/` | Get all tasks (paginated) | Yes |
| GET | `/tasks/{id}` | Get a specific task | Yes |
| PUT | `/tasks/{id}` | Update a task | Yes |
| DELETE | `/tasks/{id}` | Delete a task | Yes |

### AI
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/tasks/ai/prioritize` | AI-powered task prioritization | Yes |

### Query Parameters for GET /tasks/
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | int | 1 | Page number |
| limit | int | 10 | Results per page |
| status | string | None | Filter by status (todo/in-progress/done) |

## 🤖 AI Prioritization
The `/tasks/ai/prioritize` endpoint uses **Groq LLM (Llama 3.3-70b)** to:
- Analyze all your tasks
- Consider deadlines, status and descriptions
- Return a smart priority order with reasoning
- Provide an overall productivity summary

Example response:
```json
{
  "prioritization": "PRIORITY ORDER:\n1. ID 2 - Finish ML assignment - Earliest deadline, already in progress\n2. ID 1 - Cisco application - Deadline approaching\n3. ID 3 - Study for exam - Latest deadline\n\nSUMMARY:\nFocus on the ML assignment first..."
}
```

## 🔐 Authentication Flow
1. Register at `POST /users/register`
2. Login at `POST /users/login` → get JWT token
3. Click **Authorize** in Swagger UI and paste token
4. All protected endpoints are now accessible

## 📊 CI/CD Pipeline
Every push to `main` automatically:
- Sets up Python environment
- Installs all dependencies
- Runs all 5 pytest unit tests
- Fails the build if any test fails

## 👩‍💻 Author
**Khushi Chhabra**  
B.E. Computer Science, Thapar Institute of Engineering and Technology  
[LinkedIn](https://www.linkedin.com/in/khushichhabra7921) | [GitHub](https://github.com/khushichhabra7921)
