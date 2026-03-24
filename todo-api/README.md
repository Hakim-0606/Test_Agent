# 📝 Todo API

A simple REST API to manage tasks, built with **FastAPI** and **Python**.

## 🚀 Getting Started

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the server
```bash
uvicorn app.main:app --reload
```

### API Docs
Open your browser at: http://localhost:8000/docs

## 📦 Endpoints

| Method | Endpoint        | Description       |
|--------|-----------------|-------------------|
| GET    | /tasks          | List all tasks    |
| GET    | /tasks/{id}     | Get a task        |
| POST   | /tasks          | Create a task     |
| PUT    | /tasks/{id}     | Update a task     |
| DELETE | /tasks/{id}     | Delete a task     |

## 🧪 Run Tests
```bash
pytest tests/
```

## 🗂️ Project Structure
```
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py       # Routes
│   ├── models.py     # Pydantic schemas
│   └── database.py   # In-memory storage
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```
