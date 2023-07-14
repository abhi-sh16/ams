from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ams.database import get_db
from ams.models import *
from ams.oauth2 import get_current_user
from ams.repository import courses
from ams.schema import *

router = APIRouter(tags=["Courses"])


@router.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db),
                  auth: Users = Depends(get_current_user)):
    return courses.create(course, db)


@router.get("/get_course_id", response_model=ShowCourses)
def get_course_id(class_name: str, db: Session = Depends(get_db),
                  auth: Users = Depends(get_current_user)):
    course = db.query(Courses).filter(Courses.class_name == class_name).first()
    return courses.get_course(class_name, db)


