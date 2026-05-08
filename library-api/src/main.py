from fastapi import FastAPI 
from database import engine 
import models
from routers import books,borrow,members

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(books.router,prefix = "/books",tags = ["Books"])
app.include_router(members.router,prefix ="/members",tags = ["Members"])
app.include_router(borrow.router,prefix="/borrow",tags = ["Borrow"])