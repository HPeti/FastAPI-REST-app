from sqlalchemy.orm import Session

import models, schemas

def get_movie_by_id(db: Session, id: str):
    return db.query(models.Movie).filter(models.Movie.id == id).first()

def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    #db_movie = models.Movie(title=movie.title, year=movie.year, is_adult=movie.is_adult, runtime_minutes=movie.runtime_minutes, genres=movie.genres)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
