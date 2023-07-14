from ams import models
from ams.database import get_db
from ams.schema import *
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from ams.oauth2 import get_current_user
from ams.repository import users
router = APIRouter(tags=["Users"])


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db), auth: models.Users = Depends(get_current_user)):
    return users.create(user, db)
