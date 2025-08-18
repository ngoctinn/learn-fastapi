
from fastapi import APIRouter
from simple_postgres_app.database import SessionLocal


router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
