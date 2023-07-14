import logging
from datetime import datetime
from ams import hashing
from ams.database import get_db
from ams.models import *
from sqlalchemy.orm import Session
from ams.database import SessionLocal


def startup_event():
    # Code to be executed once when the application starts
    db = SessionLocal()
    if not db.query(Users).all():
        new_user = Users(
            type="admin",
            full_name="admin",
            username="admin",
            email="admin@email.com",
            password=hashing.Hash.bcrypt("admin"),
            submitted_by="admin",
            updated_at=datetime.now()
        )
        # Adds the user to the session and commit changes

        db.add(new_user)
        db.commit()
        # Refresh the session to get the updated user with the generated ID
        db.refresh(new_user)
        db.close()
        logging.info("username: admin@email.com , password : admin")
