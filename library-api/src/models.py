from sqlalchemy import Column ,Integer , String , Enum , Date , ForeignKey  
from database import Base
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

class Book(Base):

    __tablename__ = "book"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    total_copies = Column(Integer)
    available_copies = Column(Integer)


class Member(Base):
    
    __tablename__ = "member"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    membership_type = Column(Enum("basic","premium"))



class Borrow(Base):
     
    __tablename__ = "borrow"

    id =Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("book.id"))
    member_id = Column(Integer,ForeignKey("member.id"))
    borrowed_on = Column(Date)
    returned_on = Column(Date,nullable=True)























