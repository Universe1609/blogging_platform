from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext

#encryption
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: UserCreate):
    
def update_user(db: Session, user_id: int, user: UserUpdate):
    
def delete_user(db: Session, user_id: int):
    
def get_user(db: Session, user_id: int):