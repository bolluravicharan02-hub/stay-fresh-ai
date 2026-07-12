from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def create_tables():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    FastAPI Dependency
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()