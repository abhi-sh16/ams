from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ams.database import get_db
from ams.models import Users
from ams.oauth2 import get_current_user
from ams.repository import departments
from ams.schema import *

router = APIRouter(tags=["Departments"])


@router.post("/departments")
def create_department(department: DepartmentCreate, db: Session = Depends(get_db),
                      auth: Users = Depends(get_current_user)):
    return departments.create(department, db)
