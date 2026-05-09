from pydantic import BaseModel,ConfigDict,EmailStr,Field
from datetime import date 
from typing import Optional , Literal

class BookCreate(BaseModel):
    title : str 
    author : str 
    genre : str 
    total_copies : int 
    available_copies : int 


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    
    id : int
    title : str 
    author : str 
    genre : str 
    total_copies : int 
    available_copies : int 


class MemberCreate(BaseModel):
    name : str
    email : EmailStr
    phone : str = Field(min_length = 10 ,max_length = 10)
    membership_type : Literal["basic","premium"] = "basic"


class MemberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name : str 
    email : EmailStr
    phone : str 
    membership_type : str


class BorrowCreate(BaseModel):
    book_id : int
    member_id : int
    

class BorrowResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    book_id : int
    member_id :int
    borrowed_on :date
    returned_on : Optional[date] = None
