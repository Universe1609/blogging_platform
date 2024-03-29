from fastapi import HTTPException
from sqlalchemy.orn import Session
from 

def create_post(db: Session, post: PostCreate, user_id: int):
    try:
        #Create a post instance using pydantic model into sqlalchemy model
        db_post = Posts(**post.dic(), author_id = user_id)
        
        #add the new post
        db.add(db_post)
        
        #commit the post
        db.commit()
        
        #Refresh the instance (not sure this is a good practice or safe implementation)
        db.refresh(db_post)
        
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(Status_code = 400, detail=str(e))
    
def get_post(db: Session, post_id: int):
    db_get = db.query(Post).filter(Post.id == post_id).first()
    
    if not db_get:
        return f"Post not Found"
    
    return get

def update_post():
    
def delete_post():
    