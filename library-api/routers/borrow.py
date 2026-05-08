from fastapi import APIRouter , HTTPException,Depends
from sqlalchemy.orm import Session
import models
from schema import BorrowCreate,BorrowResponse
from database import get_db
from datetime import date

router = APIRouter()

@router.post("/",response_model=BorrowResponse)
def borrow(borrow:BorrowCreate,db:Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id==borrow.book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")

    member = db.query(models.Member).filter(models.Member.id == borrow.member_id).first()
    if not member:
        raise HTTPException(status_code=404,detail="Book not found")

    if book.available_copies == 0 :
        raise HTTPException(status_code=400,detail="Book copies exists")
        
    existing =db.query(models.Borrow).filter(
        models.Borrow.book_id == borrow.book_id,
        models.Borrow.member_id == borrow.member_id,
        models.Borrow.returned_on == None
    ).first()
    if existing:
        raise HTTPException(status_code=400,detail="already borrow book")
    
    new_borrow = models.Borrow(
        book_id = borrow.book_id,
        member_id = borrow.member_id,
        borrowed_on = date.today()
    )

    book.available_copies -= 1
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow


@router.post("/return/{record_id}",response_model = BorrowResponse)
def return_book(record_id:int ,db:Session=Depends(get_db)):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.id == record_id).first()
    if not db_borrow:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    if db_borrow.returned_on is not None:
        raise HTTPException(status_code=400,detail="Book already returned")
    db_borrow.returned_on = date.today()
    book = db.query(models.Book).filter(models.Book.id == db_borrow.book_id).first()
    book.available_copies +=1
    db.commit()
    db.refresh(db_borrow)
    return db_borrow
    

@router.get("/member/{member_id}",response_model=list[BorrowResponse])
def get_borrow_history(member_id:int,db:Session=Depends(get_db)):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.member_id == member_id).all()
    return db_borrow

