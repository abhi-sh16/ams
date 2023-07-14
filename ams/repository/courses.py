from datetime import datetime
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ams.database import get_db
from ams.models import Courses
from ams.schema import CourseCreate


def create(course: CourseCreate, db: Session = Depends(get_db)):
    # Create a new course in the database
    try:
        new_course = Courses(
            course_name=course.course_name,
            department_id=course.department_id,
            semester=course.semester,
            class_name=course.class_name,
            lecture_hours=course.lecture_hours,
            submitted_by=course.submitted_by,
            updated_at=datetime.now()
        )
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return {"message": "Course created successfully", "course_id": new_course.id}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Foreign Key Constraint Failed")


def get_course(class_name: str, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.class_name == class_name).first()
    return course if course else {"id": None}

