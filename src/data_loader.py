from database import SessionLocal, engine
from crud import create_movie
from imdb_scraper import scrape_movies
from schemas import MovieCreate
import models

models.Base.metadata.create_all(bind=engine)

def __init_db():
    return SessionLocal()

# Loads scraped movie data into database.
def __load_movies_into_db(db: SessionLocal, limit: int = 250):
    movies_list = scrape_movies(limit)
    print(len(movies_list))
    for movie in movies_list:
        print(movie)

        create_movie(db, MovieCreate(title=movie.get('title'), year=movie.get('year'), rating=movie.get('ratings'), casts=movie.get('cast')))

try:
    db = __init_db()
    __load_movies_into_db(db)
finally:
    db.close()