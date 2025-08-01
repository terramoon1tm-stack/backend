from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal

# Har bir request uchun session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
