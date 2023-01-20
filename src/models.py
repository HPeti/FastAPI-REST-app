from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, unique = True, index = True)
    year = Column(Integer)
    rating = Column(Float)
    casts = Column(String)