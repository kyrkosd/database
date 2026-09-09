"""
Database setup: engine, session, and base class.

This is the core wiring. Everything else imports from here.
Swapping to postgresql later= change DATABASE_URL only

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#Sqlite stores the whole DB in a single file (app.db) next to your code.
#For postgresql later, this becomes e.g.:
#"postgresql://user:password@localhost/mydbname"

DATABASE_URL = "sqlite:///./app.db"

#check_same_thread=False is needed only for sqlite, not for postgresql
#because the request to the DB is made from a different thread than the one that created the engine.

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

#sessionlocal() gives you a fresh database session per request

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    """All models inherit from this. Sqlalchemy uses it to track tables."""
    pass

def get_db():
    """Dependancy that hands a session to a request, then always closes it.
    Use with FastAPI's Depends(), or call manually in scripts."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
