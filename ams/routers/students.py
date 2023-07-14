from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ams import models
from ams.database import get_db
from ams.models import Users
from ams.oauth2 import get_current_user
from ams.repository import students
from ams.schema import *

router = APIRouter(tags=["Students"])


@router.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db),
                   auth: Users = Depends(get_current_user)):
    return students.create(student, db)


@router.get("/get_student_id", response_model=ShowStudents)
def get_student_id(full_name: str, class_name: str, db: Session = Depends(get_db,),
                   auth: models.Users = Depends(get_current_user)):
    return students.get_student(full_name, class_name, db)
