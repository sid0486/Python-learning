from fastapi import FastAPI 
from models import Product

app = FastAPI()

@app.get("/")
def greet ():
    return "welcom to FastAPI"


products = [
    Product(id=1, name="PHONE", description="Budget smartphone", price=20000, quantity=5),
    Product(id=2, name="LAPTOP", description="Mid-range laptop", price=60000, quantity=3),
    Product(id=3, name="HEADPHONES", description="Wireless headphones", price=3000, quantity=10),
    Product(id=6, name="SMARTWATCH", description="Fitness smartwatch", price=5000, quantity=7),
    Product(id=5, name="TABLET", description="Android tablet", price=25000, quantity=4),
    Product(id=11, name="KEYBOARD", description="Mechanical keyboard", price=4000, quantity=8),
    Product(id=7, name="MOUSE", description="Wireless mouse", price=1500, quantity=12),
    Product(id=8, name="MONITOR", description="24-inch LED monitor", price=12000, quantity=6),
    Product(id=9, name="SPEAKER", description="Bluetooth speaker", price=3500, quantity=9),
    Product(id=10, name="POWERBANK", description="10000mAh power bank", price=1200, quantity=15)
]
@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    # return products[id-1] not right  logic 
    return "Product not found "

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product/{id}")
def update_product(id: int,product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product update sucessfully"
    
    return "No product found"


@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"msg": "Product deleted"}

    return "product not found"

