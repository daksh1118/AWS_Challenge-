from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models in the application.
    Subclasses should inherit from Base.
    """
    pass
