from datetime import datetime
from ams import hashing
from ams.database import get_db
from ams.models import *
from ams.schema import *
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
from ams.oauth2 import get_current_user
from sqlalchemy.exc import IntegrityError


def create(user: UserCreate, db: Session = Depends(get_db), auth: Users = Depends(get_current_user)):
    # Create a new user in the database
    try:
        new_user = Users(
            type=user.type,
            full_name=user.full_name,
            username=user.username,
            email=user.email,
            password=hashing.Hash.bcrypt(user.password),
            submitted_by=user.submitted_by,
            updated_at=datetime.now()
        )
        # Add the user to the session and commit changes

        db.add(new_user)
        db.commit()
        # Refresh the session to get the updated user with the generated ID
        db.refresh(new_user)
        return {"message": "User created successfully", "user_id": new_user.id}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Unique Key Constraint Failed")
