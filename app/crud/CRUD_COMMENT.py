from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.comment import Comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def create_comment(db: Session, comment: CommentCreate, user_id: int, post_id: int):
    
    #remember implement try, except
    db_comment = Comment(**comment.dict(), user_id=user_id, post_id=post_id)
    
    db.add(db_comment)
    
    db.commit()
    
    db.refresh(db_comment)
    
    return db_comment

def update_comment(db: Session, comment_id: int, comment: CommentUpdate, user_id: int):
    db_comment = get_comment(db, comment_id)
    if not db_comment or db_comment.user_id != user_id:
        raise HTTPException(status_code=404, detail="Comment not found or user not authorized")
    comment_data = comment.dict(exclude_unset=True)
    for key, value in comment_data.items():
        setattr(db_comment, key, value)
    db.commit()
    return db_comment

def delete_comment(db: Session, comment_id: int, user_id: int):
    db_comment = get_comment(db, comment_id)
    if not db_comment or db_comment.user_id != user_id:
        raise HTTPException(status_code=404, detail="Comment not found or user not authorized")
    db.delete(db_comment)
    db.commit()
