# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from models import Student
# from database import get_db
# import database_models

# router = APIRouter()

# _seed = [
#     {"id": 1, "name": "siddhi",    "std": 10, "address": "laxmi nagar",     "mobile": "9313429179"},
#     {"id": 2, "name": "dhananjay", "std": 10, "address": None,              "mobile": "9313429549"},
#     {"id": 3, "name": "pooja",     "std": 10, "address": "millenium nagar", "mobile": "9313259179"},
#     {"id": 4, "name": "sammy",     "std": 10, "address": "ramayan park",    "mobile": "9312329179"},
# ]


# def seed(db: Session):
#     if db.query(database_models.Student).count() == 0:
#         db.add_all([database_models.Student(**s) for s in _seed])
#         db.commit()


# @router.get("/", response_model=list[Student])
# def get_all_students(db: Session = Depends(get_db)):
#     seed(db)
#     return db.query(database_models.Student).all()


# @router.get("/{id}", response_model=Student)
# def get_student(id: int, db: Session = Depends(get_db)):
#     row = db.query(database_models.Student).filter(database_models.Student.id == id).first()
#     if not row:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return row


# @router.post("/", response_model=Student, status_code=201)
# def add_student(student: Student, db: Session = Depends(get_db)):
#     row = database_models.Student(**student.model_dump())
#     db.add(row)
#     db.commit()
#     db.refresh(row)
#     return row


# @router.put("/{id}", response_model=Student)
# def update_student(id: int, student: Student, db: Session = Depends(get_db)):
#     row = db.query(database_models.Student).filter(database_models.Student.id == id).first()
#     if not row:
#         raise HTTPException(status_code=404, detail="Student not found")
#     for k, v in student.model_dump().items():
#         setattr(row, k, v)
#     db.commit()
#     db.refresh(row)
#     return row


# @router.delete("/{id}")
# def delete_student(id: int, db: Session = Depends(get_db)):
#     row = db.query(database_models.Student).filter(database_models.Student.id == id).first()
#     if not row:
#         raise HTTPException(status_code=404, detail="Student not found")
#     db.delete(row)
#     db.commit()
#     return {"message": "Student deleted"}