from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy import relationship
from ..db.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Comments(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    user = relationship("Users", back_populates="comments")
    post = relationship("Posts", back_populates="comments") 