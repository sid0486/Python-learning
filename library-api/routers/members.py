from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src import models
from src.schema import MemberCreate, MemberResponse
from src.database import get_db

router = APIRouter()

@router.get("/",response_model=list[MemberResponse])
def get_all_member(db:Session=Depends(get_db)):
    return db.query(models.Member).order_by(models.Member.id).all()

@router.get("/{id}",response_model=MemberResponse)
def get_by_id(id:int,db:Session=Depends(get_db)):
    db_member = db.query(models.Member).filter(models.Member.id == id).first()
    if not db_member:
        raise HTTPException(status_code=404,detail="Member Not Found")
    return db_member

@router.post("/",response_model=MemberResponse)
def add_member(member:MemberCreate,db:Session=Depends(get_db)):
    db_member = db.query(models.Member).filter(models.Member.name == member.name).first()
    if db_member:
        raise HTTPException(status_code=400,detail="Member already exists")
    new_member= models.Member(**member.model_dump())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

@router.put("/{id}",response_model=MemberResponse)
def update_member(id:int,member:MemberCreate,db:Session=Depends(get_db)):
    db_member = db.query(models.Member).filter(models.Member.id == id).first()
    if not db_member:
        raise HTTPException(status_code=404,detail="Member not found")
    db_member.name = member.name
    db_member.email = member.email
    db_member.phone = member.phone
    db_member.membership_type = member.membership_type
    db.commit()
    db.refresh(db_member)
    return db_member

@router.delete("/{id}")
def delete_member(id:int,db:Session=Depends(get_db)):
    db_member = db.query(models.Member).filter(models.Member.id == id).first()
    if not db_member:
        raise HTTPException(status_code=404,detail="Member not found")
    db.delete(db_member)
    db.commit()
    return {"message":"Member deleted sucessfully"}
