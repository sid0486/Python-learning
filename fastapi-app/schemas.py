from pydantic import BaseModel , ConfigDict , Field ,field_validator,computed_field
from typing import Optional 

class ProductCreate(BaseModel):
    name:str 
    description:Optional[str] = None 
    price : float 
    quantity : int


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    @computed_field
    @property
    def total_value(self) -> float:
        return self.price * self.quantity

class Address(BaseModel):
    city: str
    pincode: str

class StudentCreate(BaseModel):
    name : str
    std : int 
    address : Address 
    mobile : str =  Field(min_length = 10 , max_length = 10)

    @field_validator("mobile")
    @classmethod
    def mobile_must_be_digits(cls,v):
        if not v.isdigit():
            raise ValueError("Mobile must contain only digits")
        return v

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int 
    name : str
    std : int 
    address : str
    mobile : str





# from pydantic import BaseModel, model_validator

# class BookingCreate(BaseModel):
#     check_in: int   # day number
#     check_out: int

#     @model_validator(mode="after")
#     def check_out_must_be_after_check_in(self):
#         if self.check_out <= self.check_in:
#             raise ValueError("check_out must be after check_in")
#         return self
# when one field depends on another. field_validator can only see one field at a time — model_validator sees the whole model.




















