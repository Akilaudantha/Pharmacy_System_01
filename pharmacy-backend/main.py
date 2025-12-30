from fastapi import FastAPI
from database import engine, Base
from models import User

app = FastAPI()

# Create tables in MySQL (if not exist)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello, Pharmacy System!"}
