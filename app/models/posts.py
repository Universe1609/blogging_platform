from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy import relationship
from sqlalchemy.sql import func
from ..db.database import Base

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(100), index = True, nullable = True)
    content = Column(Text, nullable= False)
    timestamp = Column(Datetime, default=func.now(), nullable = True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationship back to the user
    users = relationship("Users", back_populates="posts")
    comments = relationship("Comments", back_populates="posts")
