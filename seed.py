"""
Quick standalone test of the database, no web server needed.
 
Run from the project root:   python seed.py
 
It creates the tables, adds a user and a post, then reads them back.
Great for confirming everything works before touching the API.
"""

from app.database import Base, engine, SessionalLocal
from app import crud

def main():
    Base.metadata.create_all(bind=engine)

    db = SessionalLocal()
    try:
        existing = crud.get_user_by_email(db, "test@example.com")
        if existing is None:
            user = crud.create_user(db, email="test@example.com", name="Test User")
            print(f"Create user: id ={user.id}, {user.name}")

            post = crud.create_post(
                db,
                tittle="First Post",
                content="This is the first post.",
                author_id=user.id,
            )
            print(f"Create post: id={post.id}, '{post.tittle}'")
        else:
            user = existing
            print(f"User already exists: id={user.id}, {user.name}")

        print("\nAll users:")
        for u in crud.list_users(db):
            print(f"  - {u.id}: {u.name} <{u.email}> ({len(u.posts)} posts)")   

    finally:
        db.close()
 
 
if __name__ == "__main__":
    main()
        