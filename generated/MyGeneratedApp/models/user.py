from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    SQLAlchemy model for User.
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    

    def __repr__(self):
        return f"<User(id={self.id})>"