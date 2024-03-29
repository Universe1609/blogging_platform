from pydantic import BaseModel
from datetime import datetime
from typing import List

class PostBase(BaseModel):
    title: str
    content: str
    
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    timestamp: datetime
    author_id: int
    #comments: List['Comment'] = []
    
    class Config:
        orm_mode = True