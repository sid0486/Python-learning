from fastapi import FastAPI, HTTPException , Depends
from models import Product, Student
from database import session, engine
import database_models
from app.routers import products, students
from sqlalchemy.orm import Session

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

# app.include_router(products.router, prefix="/products", tags=["Products"])
# app.include_router(students.router, prefix="/students", tags=["Students"])

# ---- PRODUCTS ----
products = [
    {"id": 1, "name": "PHONE", "description": "Budget smartphone", "price": 20000, "quantity": 5},
    {"id": 2, "name": "LAPTOP", "description": "Mid-range laptop", "price": 60000, "quantity": 3},
    {"id": 3, "name": "HEADPHONES", "description": "Wireless headphones", "price": 3000, "quantity": 10},
    {"id": 4, "name": "TABLET", "description": "Android tablet", "price": 25000, "quantity": 7},
    {"id": 5, "name": "SMARTWATCH", "description": "Fitness tracker", "price": 5000, "quantity": 15}
]
counter = 6  # next id starts from 6
def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()

def get_db():
    db = session ()
    try :
        yield db 
    finally :
        db.close()


@app.get("/")
def greet():
    return "Welcome to fastapi"


@app.get("/products")
def get_all_products(db :Session = Depends(get_db)):
    db_product = db.query(database_models.Product).order_by(database_models.Product.id).all()
    # SELECT * FROM product ORDER BY id;
    return db_products

@app.get("/product/{id}")
def get_product(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    # SELECT * FROM product WHERE id = 2 LIMIT 1;
    # db.query(Product).filter(Product.id == 2).first()
    if db_product:
        return db_product
    # for product in products:
    #     if product['id'] == id:

    raise HTTPException(status_code = 404,detail = "Product not found")


@app.post("/product")
def add_product(product : Product , db:Session = Depends(get_db)):
    new_product = database_models.Product(**product.model_dump())
    db_add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
    # db.add(database_models.Product(**product.model_dump()))
    # db.commit()
    # return product
    # global counter
    # # check if name already exists
    # for p in products:
    #     if p["name"].lower() == product.name.lower():
    #         raise HTTPException(status_code=400, detail="Product already exists")
    # new_product = {"id":counter,**product.model_dump()}
    # products.append(new_product)
    # counter += 1
    # return new_product

@app.put("/product/{id}")
def update_product(id:int,product:Product,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return db_product
    # if db_product :
    #     db_product.name = product.name
    #     db_product.description = product.description
    #     db_product.price = product.price
    #     db_product.quantity = product.quantity
    #     db.commit()
    # else:
    #     raise HTTPException(status_code = 404,detail = "Product not found")

    # for i in range(len(products)):
    #     if products[i]["id"] == id :
    #         products[i].update(product.model_dump())
    #         return products[i]
    # raise HTTPException(status_code=404,detail= "Product not found")


@app.delete("/product/{id}")
def delete_product(id:int):
    db_product= db.query(database_models.product).filter(database_models.product.id==id).first()
    if not db_product:
        raise HTTPException(status_code=404 , detail = "Product not found")
    db.delete(db_product)
    db.commit()
    return{"message": f"Product {id} deleted"}

    # for i in range(len(products)):
    #     if products[i]["id"] == id:
    #         del products[i]
    #         return {"message": f"Product {id} deleted"}
    raise HTTPException(status_code=404, detail="Product not found")


# ---- STUDENTS ----

students = [
    Student(id=1, name="siddhi", std=10, address="laxmi nagar", mobile="9313429179"),
    Student(id=2, name="dhananjay", std=10, address="", mobile="9313429549"),
    Student(id=3, name="pooja", std=10, address="millenium nagar", mobile="9313259179"),
    Student(id=4, name="sammy", std=10, address="ramayan park", mobile="9312329179")
]

@app.get("/students")
def get_all_students():
    return students

@app.get("/student")
def get_student_by_id(id: int):
    for student in students:
        if student.id == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/student")
def add_student(student: Student):
    students.append(student)
    return student

@app.put("/student/{id}")
def update_student(id: int, student: Student):
    for i in range(len(students)):
        if students[i].id == id:
            students[i] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/student/{id}")
def delete_student(id: int):
    for i in range(len(students)):
        if students[i].id == id:
            del students[i]
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")