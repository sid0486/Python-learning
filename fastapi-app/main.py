from fastapi import FastAPI
from models import Product
from models import Student
from fastapi import FastAPI, HTTPException  # ✅ make sure HTTPException is imported
from database import session,engine
import database_models


app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet ():
    return "welcome to FASTAPI!!!!"

products = [
    Product(id=1, name="PHONE", description="Budget smartphone", price=20000, quantity=5),
    Product(id=2, name="LAPTOP", description="Mid-range laptop", price=60000, quantity=3),
    Product(id=3, name="HEADPHONES", description="Wireless headphones", price=3000, quantity=10)
]

def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0 :
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()


@app.get("/products")
def get_all_products():
    # db = session()
    # db.query()
    return products


@app.get("/product")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product

@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product

@app.put("/product/{id}")
# "Find item by id → replace it → return updated → if not found raise 404"
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return product
    return "NOT FOUND "


@app.delete("/product/{id}")
# "Find item by id → delete it → return message → if not found raise 404"
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id :
            del products[i]
            return {"message":"Deleted"}
    return "not found "

# ADD    → append → return item
# UPDATE → find index → replace → return item
# DELETE → find index → del → return message
# ALL    → raise 404 if not found


@app.get("/")
def greet ():
    return "Welcome students"

students = [
    Student(id=1,name="siddhi",std=10,address="laxmi nagar",mobile="9313429179"),
    Student(id=2,name="dhananjay",std=10,address="",mobile="9313429549"),
    Student(id=3,name="pooja",std=10,address="millenium nagar",mobile="9313259179"),
    Student(id=4,name="sammy",std=10,address="ramayan park",mobile="9312329179")
]


@app.get("/students")
def get_all_students():
    return students

@app.get("/student")
def get_student_by_id (id:int):
    for student in students:
        if student.id == id :
            return student


@app.post("/student/{id}")
def add_student(student:Student):
    students.append(student)
    return student

@app.put("/student/{id}")
def update_student(id:int,student:Student):
    for i in range(len(students)):
        if students[i].id == id :
            students[i] = student
            return student
    return "Student Not FOUND"

@app.delete("/student/{id}")
def delete_student(id:int):
    for i in range(len(students)):
        if students[i].id == id :
            del students[i]
            return {"message":"Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")



























