from pydantic import BaseModel, fields
from typing import Optional


class UserCreate(BaseModel):
    type: str
    full_name: str
    username: str
    email: str
    password: str
    submitted_by: str


class DepartmentCreate(BaseModel):
    department_name: str
    submitted_by: str


class CourseCreate(BaseModel):
    course_name: str
    department_id: int
    semester: str
    class_name: str
    lecture_hours: str
    submitted_by: str


class StudentCreate(BaseModel):
    full_name: str
    department_id: int
    class_name: str
    submitted_by: str


class AttendanceLogCreate(BaseModel):
    student_id: int
    course_id: int
    present: bool
    submitted_by: str


class ShowStudents(BaseModel):
    id: int

    class Config:
        from_attributes = True


class ShowCourses(BaseModel):
    id: Optional[int]

    class Config:
        from_attributes = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
