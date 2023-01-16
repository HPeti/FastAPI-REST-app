from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, unique = True, index = True)
    year = Column(Integer)
    is_adult = Column(Boolean, default=False)
    runtime_minutes = Column(Integer)
    genres = Column(String)

#class Movie(Base):
#    __tablename__ = "movies"
#
#    tconst = Column(String, primary_key=True, index = True)
#    titleType = Column(String)
#    primaryTitle = Column(String, unique = True, index = True)
#    originalTitle = Column(String, unique = True, index = True)
#    isAdult = Column(String)
#    startYear = Column(String)
#    endYear = Column(String)
#    runtimeMinutes = Column(String)
#    genres = Column(String)