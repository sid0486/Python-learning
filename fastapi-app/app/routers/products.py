from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Product
from database import get_db
import database_models

router = APIRouter()

_seed = [
    {"id": 1, "name": "PHONE",      "description": "Budget smartphone",   "price": 20000, "quantity": 5},
    {"id": 2, "name": "LAPTOP",     "description": "Mid-range laptop",    "price": 60000, "quantity": 3},
    {"id": 3, "name": "HEADPHONES", "description": "Wireless headphones", "price":  3000, "quantity": 10},
]


def seed(db: Session):
    if db.query(database_models.Product).count() == 0:
        db.add_all([database_models.Product(**p) for p in _seed])
        db.commit()


@router.get("/", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    seed(db)
    return db.query(database_models.Product).all()


@router.get("/{id}", response_model=Product)
def get_product(id: int, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    return row


@router.post("/", response_model=Product, status_code=201)
def add_product(product: Product, db: Session = Depends(get_db)):
    row = database_models.Product(**product.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.put("/{id}", response_model=Product)
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    for k, v in product.model_dump().items():
        setattr(row, k, v)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    row = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(row)
    db.commit()
    return {"message": "Product deleted"}