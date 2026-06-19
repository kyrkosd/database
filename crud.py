"""
CRUD = Create, Read, Update, Delete.
 
These are plain functions that take a session and do one thing each.
Keeping DB logic here (not in your API routes) keeps everything testable
and reusable. Your web routes just call these.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import select

from . import models

#---users--

def create_user(db: Session, email:str, name:str) -> models.User:
    """Create a new user and return it."""
    user = models.User(email=email, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id:str) -> models.User | None:
    return db.execute(select(models.User).where(models.User.id == user_id)).scalars().first()

def list_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    stmt = select(model.User).offset(skip).limit(limit)
    return list(db.scalars(stmt)).all())

def delete_user(db: Session, user_id: int) -> bool:
    user = db.get(models.User, user_id)
    if user is None:
       return False
    db.delete(user)
    db.commit()
    return True


#---posts---

def create_post(db: Session, tittle: str, content: str, author_id: int) -> models.Post:
    post = models.Post(tittle=tittle, content=content, author_id=author_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def list_posts(db: Session, skip: int = 0, limit : int = 100) -> list[models.Post]:
    stmt = select(models.Post).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())