from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()

class MembershipType(str, enum.Enum):
    basic = "basic"
    premium = "premium"

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    author = Column(String(100))
    genre = Column(String(100))
    total_copies = Column(Integer)
    available_copies = Column(Integer)

class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(255), unique=True)
    phone = Column(String(15))
    membership_type = Column(Enum(MembershipType, name="membership_type"))

class Borrow(Base):
    __tablename__ = "borrow"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    member_id = Column(Integer, ForeignKey("member.id"))
    borrowed_on = Column(Date)
    returned_on = Column(Date, nullable=True)