from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from database import engine
from models import Todos
import models
from database import SessionLocal

router = APIRouter(
    prefix="todos",
    tags=["todos"],
    responses={404:{"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        

