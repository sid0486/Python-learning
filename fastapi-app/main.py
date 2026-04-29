from fastapi import FastAPI
import database_models
from database import engine
from routers import products, students
# from routers.products import memory_router
# from routers.students import students_memory_router

# ---- APP SETUP ----
app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

# ---- INCLUDE ROUTERS ----
app.include_router(products.router, prefix="/products", tags=["Products"])
# prefix="/products" means all product routes start with /products
# GET / → becomes GET /products
# GET /{id} → becomes GET /products/{id}
# tags=["Products"] → groups routes in Swagger UI

app.include_router(students.router, prefix="/students", tags=["Students"])
# same pattern for students
# GET / → becomes GET /students
# POST / → becomes POST /students

# ---- GREET ----
@app.get("/")
def greet():
    return "Welcome to FastAPI!"