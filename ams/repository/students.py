from datetime import datetime
from ams.database import get_db
from ams.models import *
from ams.schema import *
from sqlalchemy.orm import Session
from fastapi import Depends


def create(student: StudentCreate, db: Session = Depends(get_db)):
    # Create a new student in the database
    new_student = Students(
        full_name=student.full_name,
        department_id=student.department_id,
        class_name=student.class_name,
        submitted_by=student.submitted_by,
        updated_at=datetime.now()
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student created successfully", "student_id": new_student.id}


def get_student(full_name: str, class_name: str, db: Session = Depends(get_db)):
    # Gets student_id from full_name and class_name in the database
    return db.query(Students).filter(Students.full_name == full_name and Students.class_name == class_name).first()
