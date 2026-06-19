"""
Models = your database tables, written as Python classes.
 
Each class is a table. Each attribute is a column.
Edit these to match whatever your app actually stores.
The User/Post example shows a one-to-many relationship.
"""

from datetime import datetime, timezone
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped

from .databaseBase, 

def _now():
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(225), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)

    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
        )
    
    class Post(Base):
        __tablename__="posts"
    
        id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
        title: Mapped[str] = mapped_column(String(200))
        content: Mapped[str] = mapped_column(Text)
        created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)

        #the foreign key column+the relationship back to User

        author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
        author: Mapped["User"] = relationship(back_populates="posts")