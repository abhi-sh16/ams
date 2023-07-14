from ams.database import Base
from sqlalchemy import Column, String, Boolean, INTEGER, ForeignKey, DateTime


class Users(Base):
    __tablename__ = "Users"
    id = Column(INTEGER, primary_key=True, index=True)
    type = Column(String)
    full_name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime)


class Departments(Base):
    __tablename__ = "Departments"
    id = Column(INTEGER, primary_key=True, index=True)
    department_name = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime)


class Courses(Base):
    __tablename__ = "Courses"
    id = Column(INTEGER, primary_key=True, index=True)
    course_name = Column(String)
    department_id = Column(INTEGER, ForeignKey("Departments.id"))
    semester = Column(String)
    class_name = Column(String)
    lecture_hours = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime)


class Students(Base):
    __tablename__ = "Students"
    id = Column(INTEGER, primary_key=True, index=True)
    full_name = Column(String)
    department_id = Column(INTEGER)
    class_name = Column(INTEGER)
    submitted_by = Column(String)
    updated_at = Column(DateTime)


class AttendanceLog(Base):
    __tablename__ = "Attendance_log"
    id = Column(INTEGER, primary_key=True, index=True)
    student_id = Column(INTEGER, ForeignKey("Students.id"))
    course_id = Column(INTEGER, ForeignKey("Courses.id"))
    present = Column(Boolean)
    submitted_by = Column(String)
    updated_at = Column(DateTime)

