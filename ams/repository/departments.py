from datetime import datetime
from ams.database import get_db
from ams.models import *
from ams.schema import *
from sqlalchemy.orm import Session
from fastapi import Depends


def create(department: DepartmentCreate, db: Session = Depends(get_db)):
    # Create a new department in the database
    new_department = Departments(
        department_name=department.department_name,
        submitted_by=department.submitted_by,
        updated_at=datetime.now()
    )
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return {"message": "Department created successfully", "department_id": new_department.id}
