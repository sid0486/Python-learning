from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None   
    name: str
    description: str
    price: float
    quantity: int

    # def __init__(self,id:int,name:str,description:str,price:float,quantity:int):
    #     self.id = id 
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

class Student(BaseModel):
    id: Optional[int] = None   # ✅ make optional
    name: str
    std: int
    address: Optional[str] = None
    mobile: str