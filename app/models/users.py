from sqlalchemy import Column, Integer, String
from sqlalchemy import relationship
from ..db.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50), unique=True, index=True, nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=True)
    password = Column(String(25), nullable=True)
    
    #One to many relationshio with Post table and comments table
    posts = relationship("Posts", back_populates="users")
    comments = relationship("Comments", back_populates="users")
    
    def set_password(self, password):
        self.password = pwd_context.hash(password)
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.password)