from fastapi import APIRouter, HTTPException ,Depends 
from sqlalchemy.orm import Session
import database_models
from database import session
from models import Student

students_memory = [
    {"id": 1, "name": "Siddhi", "std": 10, "address": "Laxmi Nagar", "mobile": "9313429179"},
    {"id": 2, "name": "Dhananjay", "std": 10, "address": "Ramayan Park", "mobile": "9313429549"},
    {"id": 3, "name": "Pooja", "std": 11, "address": "Millenium Nagar", "mobile": "9313259179"},
]
student_counter = 4

students_memory_router = APIRouter()

@students_memory_router.get("/")
def get_all_students_memory():
    return students_memory

@students_memory_router.get("/{id}")
def get_student_memory(id:int):
    for student in students_memory:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404,detail = "Student not found")


@students_memory_router.post("/")
def add_student_memory(student : Student):
    global student_counter
    for s in students_memory:
        if s["name"].lower() == student.name.lower():
            raise HTTPException(status_code = 400 , detail = "Student already exists")
    new_student = {"id":student_counter , **student.model_dump()}
    students_memory.append(new_student)
    student_counter += 1
    return new_student


@students_memory_router.put("/{id}")
def update_student_memory(id:int,student:Student):
    for i in range(len(students_memory)):
        if students_memory[i]["id"] == id :
            students_memory[i].update(student.model_dump())
            return students_memory[i]
    raise HTTPException(status_code=404 , detail = "Student not found")


@students_memory_router.delete("/{id}")
def delete_student_memory(id:int):
    for i in range(len(students_memory)):
        if students_memory[i]["id"] == id :
            del students_memory[i]
            return {"message": f"Student {id} deleted"}
    raise HTTPException(status_code=404 ,detail= "Student not found")


router = APIRouter()

def get_db():
    db = session()
    try:
        yield db 
    finally:
        db.close()


@router.get("/")
def get_all_students(db:Session=Depends(get_db)):
    return db.query(database_models.Student).order_by(database_models.Student.id).all()

@router.get("/{id}")
def get_student(id:int , db:Session = Depends(get_db)):
    db_student = db.query(database_models.Student).filter(database_models.Student.id == id).first()
    if not db_student:
        raise HTTPException(status_code=404 , detail = "Student not found")
    return db_student

@router.post("/")
def add_student(student: Student, db: Session = Depends(get_db)):
    existing = db.query(database_models.Student).filter(
        database_models.Student.name == student.name
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Student already exists")

    new_student = database_models.Student(
        name=student.name,
        std=student.std,
        address=student.address,
        mobile=student.mobile
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.put("/{id}")
def update_student(id: int, student: Student, db: Session = Depends(get_db)):
    db_student = db.query(database_models.Student).filter(
        database_models.Student.id == id
    ).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    db_student.name = student.name
    db_student.std = student.std
    db_student.address = student.address
    db_student.mobile = student.mobile

    db.commit()
    db.refresh(db_student)

    return db_student


@router.delete("/{id}")
def delete_student(id:int, db:Session= Depends(get_db)):
    db_student = db.query(database_models.Student).filter(database_models.Student.id == id).first()
    if not db_student:
        raise HTTPException(status_code=404 , detail= "Student not found")
    db.delete (db_student)
    db.commit()
    return {"message": f"Student {id} deleted"}






































































































