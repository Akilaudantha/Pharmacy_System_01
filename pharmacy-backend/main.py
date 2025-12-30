from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User

app = FastAPI()

@app.post("/login")
def login(
    email: str, 
    password: str, 
    db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {
        "message": f"Login successful! Welcome {user.name}", 
        "role": user.role
    }
