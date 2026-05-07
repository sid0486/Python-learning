from pydantic import Basemodel,ConfigDict,EmailStr,Field
from datetime import date 
from typing import Optional , Literal

class BookCreate(Basemodel):
    title : str 
    author : str 
    genre : str 
    total_copies : int 
    available_copies : int 


class BookResponse(Basemodel):
    model_config = ConfigDict(from_attributes = True)
    
    id : int
    title : str 
    author : str 
    genre : str 
    total_copies : int 
    available_copies : int 


class MemberBook(Basemodel):
    name : str
    email : EmailStr
    phone : str = Field(min_length = 10 ,max_length = 10)
    membership_type : Literal["basic","premium"] = "basic"


class MemberResponse(Basemodel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name : str 
    email : EmailStr
    phone : str 
    membership_type : str


class BorrowCreate(Basemodel):
    book_id : int
    member_id = int
    

class BorrowResponse(Basemodel):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    book_id : int
    member_id :int
    borrowed_on :date
    returned_on : Optional[date] = None
