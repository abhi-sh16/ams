from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import ams.schema as schema
from ams.database import get_db
from ams.models import AttendanceLog
from datetime import datetime
from sqlalchemy.exc import IntegrityError


def create(attendance_log: schema.AttendanceLogCreate, db: Session = Depends(get_db)):
    # Create a new attendance log in the database
    try:
        new_attendance_log = AttendanceLog(
            student_id=attendance_log.student_id,
            course_id=attendance_log.course_id,
            present=attendance_log.present,
            submitted_by=attendance_log.submitted_by,
            updated_at=datetime.now()
        )
        db.add(new_attendance_log)
        db.commit()
        db.refresh(new_attendance_log)
        return {"message": "Attendance log created successfully", "attendance_log_id": new_attendance_log.id}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Foreign Key Constraint Failed")

