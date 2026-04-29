from fastapi import APIRouter , HTTPException ,Depends
# APIRouter = creates a mini router for this file only
# same as FastAPI but for sub-routes

from sqlalchemy.orm import Session
import database_models
from database import session
from models import Product


# in-memory list for practice
products_memory = [
    {"id": 1, "name": "PHONE", "description": "Budget smartphone", "price": 20000, "quantity": 5},
    {"id": 2, "name": "LAPTOP", "description": "Mid-range laptop", "price": 60000, "quantity": 3},
    {"id": 3, "name": "HEADPHONES", "description": "Wireless headphones", "price": 3000, "quantity": 10},
]
product_counter = 4
# counter tracks next id for in-memory products

memory_router = APIRouter()

@memory_router.get("/")
def get_all_products_memory():
    return products_memory
    # just return the list — no DB needed


@memory_router.get("/{id}")
def get_product_memory(id:int):
    for product in products_memory:
        if product["id"] == id:
            return product
    raise HTTPException(status_code=404 , detail= "Product not found")


@memory_router.post("/")
def add_product_memory(product:Product):
    global product_counter 
    for p in products_memory:
        if p["name"].lower() == product.name.lower():
            raise HTTPException(status_code = 400 , detail = "Product already exists")

    new_product = {"id":product_counter,**product.model_dump()}
    # product_counter = id
    # **product.model_dump() = spreads all fields
    # result: {"id": 4, "name": "CAMERA" ...}
    products_memory.append(new_product)
    product_counter += 1
    return new_product


@memory_router.put("/{id}")
def update_product_memory(id:int,product : Product):
    for i in range(len(products_memory)):
        # range(len()) gives index
        # need index to modify list item
        if products_memory[i]["id"] == id:
            products_memory[i].update(product.model_dump())
        # replace all fields with new values
            return products_memory[i]
    raise HTTPException(status_code=404 , detail = "Product not found")


@memory_router.delete("/{id}")
def delete_product_memory(id:int):
    for i in range(len(products_memory)):
        if products_memory[i]["id"] == id:
            del products_memory[i]
            # permanently remove from list
            return {"message": f"Product {id} deleted"}
    raise HTTPException(status_code=404 , detail = "Product not found")



# ---- CREATE ROUTER ----
router = APIRouter()
# router = like a mini app
# all routes defined here will be registered on this router
# main.py will include this router later

def get_db():
    db = session()
    try :
        yield db 
    finally:
        db.close()

@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return db_product


@router.post("/")
def add_product(product: Product, db: Session = Depends(get_db)):
    new_product = database_models.Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.put("/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return {"message": f"Product {id} deleted"}
































