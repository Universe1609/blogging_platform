from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    
class UserCreate(BaseModel):
    password: str
    
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True