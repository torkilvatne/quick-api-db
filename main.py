from typing import Optional, List

from fastapi import FastAPI, status, HTTPException
from schemas import Student
from database import SessionLocal
import models

app = FastAPI()

db = SessionLocal()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/students", response_model=List[Student], status_code=status.HTTP_200_OK)
def get_all_students():
    students=db.query(models.Student).all()

    return students


@app.get("/student/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_item(student_id: int, q: Optional[str] = None):
    student=db.query(models.Student).filter(models.Student.id == student_id).first()

    return student