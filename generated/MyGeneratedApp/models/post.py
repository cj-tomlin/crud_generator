from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    """
    SQLAlchemy model for Post.
    """
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return f"<Post(id={self.id})>"