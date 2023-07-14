from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ams.database import get_db
from ams.models import Users
from ams.oauth2 import get_current_user
from ams.schema import AttendanceLogCreate
from ams.repository import attendance_log

router = APIRouter(tags=["Attendance Log"])


@router.post("/attendance-logs")
def create_attendance_log(new_attendance_log: AttendanceLogCreate, db: Session = Depends(get_db),
                          auth: Users = Depends(get_current_user)):
    return attendance_log.create(new_attendance_log, db)


