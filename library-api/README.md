# 📚 Library Management API

A production-grade REST API built with **FastAPI** and **PostgreSQL** — featuring full library management with books, members, and borrow/return tracking.

---

## 🚀 Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | High-performance Python web framework |
| **PostgreSQL** | Production database |
| **SQLAlchemy** | Database ORM |
| **Alembic** | Database migrations — no data loss |
| **Pydantic** | Data validation and serialization |
| **Docker** | Containerized deployment |
| **pgAdmin** | Database management UI |

---

## ✨ Features

- 📖 **Books** — Add, search, update, and delete books with copy tracking
- 👥 **Members** — Register members with Basic/Premium membership types
- 🔄 **Borrow & Return** — Full borrow/return system with availability tracking
- 🛡️ **Validation** — Email uniqueness, mobile number validation, duplicate borrow prevention
- 📊 **Borrow History** — Track complete borrow history per member
- 🗄️ **Migrations** — Alembic migrations for safe schema changes

---

## 📁 Project Structure

```
library-api/
├── alembic/                  # Database migrations
│   └── versions/             # Migration files
├── routers/                  # API route handlers
│   ├── books.py              # Book CRUD + search
│   ├── members.py            # Member management
│   └── borrow.py             # Borrow/return logic
├── src/
│   ├── models.py             # SQLAlchemy DB models
│   ├── schema.py             # Pydantic schemas
│   ├── database.py           # DB connection
│   └── main.py               # FastAPI app entry point
├── .env.example              # Environment variables template
├── alembic.ini               # Alembic configuration
└── requirements.txt          # Python dependencies
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.12+
- PostgreSQL 15+
- Git

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/library-api.git
cd library-api
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your actual values
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/library_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=library_db
SECRET_KEY=your-secret-key-here
```

### 5. Run database migrations
```bash
# Apply all migrations
alembic upgrade head
```

### 6. Start the server
```bash
uvicorn src.main:app --reload
```

Visit **http://127.0.0.1:8000/docs** for interactive API documentation.

---

## 🐳 Docker Setup

### Run with Docker Compose
```bash
# Start all services (FastAPI + PostgreSQL)
docker compose up --build

# Stop all services
docker compose down
```

Visit **http://localhost:8000/docs**

---

## 📡 API Endpoints

### Books
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books/` | Get all books |
| `GET` | `/books/{id}` | Get book by ID |
| `GET` | `/books/search` | Search books |
| `POST` | `/books/` | Add a new book |
| `PUT` | `/books/{id}` | Update book |
| `DELETE` | `/books/{id}` | Delete book |

### Members
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/members/` | Get all members |
| `GET` | `/members/{id}` | Get member by ID |
| `POST` | `/members/` | Register member |
| `PUT` | `/members/{id}` | Update member |
| `DELETE` | `/members/{id}` | Delete member |

### Borrow
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/borrow/` | Borrow a book |
| `POST` | `/borrow/return/{id}` | Return a book |
| `GET` | `/borrow/member/{id}` | Get borrow history |

---

## 🗄️ Database Migrations with Alembic

```bash
# Generate a new migration after model changes
alembic revision --autogenerate -m "description of change"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history
```

> ✅ Never use `drop_all` in production. Alembic handles all schema changes safely without data loss.

---

## 🧠 Key Concepts Used

**Pydantic Schemas** — Separate `Create` and `Response` schemas for clean API contracts:
```python
class BookCreate(BaseModel):
    title: str        # user sends this — no id
    author: str

class BookResponse(BaseModel):
    id: int           # API returns this — includes id
    title: str
    model_config = ConfigDict(from_attributes=True)
```

**Dependency Injection** — Database session injected into every route:
```python
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
```

**Business Logic** — Availability tracking on every borrow/return:
```python
# On borrow
book.available_copies -= 1

# On return
book.available_copies += 1
```

---

## 📝 Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost/db` |
| `POSTGRES_USER` | Database username | `postgres` |
| `POSTGRES_PASSWORD` | Database password | `yourpassword` |
| `POSTGRES_DB` | Database name | `library_db` |
| `SECRET_KEY` | App secret key | `generate with secrets.token_hex(32)` |

---

## 🛣️ Roadmap

- [ ] JWT Authentication
- [ ] Async SQLAlchemy
- [ ] Rate limiting
- [ ] Unit tests with pytest
- [ ] CI/CD with GitHub Actions

---

## 👨‍💻 Author

**Siddhi Patil** — Building production-grade backends as part of my AI Engineer roadmap.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/yourusername)