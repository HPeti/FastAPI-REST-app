from bs4 import BeautifulSoup
import requests
import re

# Constants
SCRAPE_URL = 'https://www.imdb.com/chart/top/'

# Scrapes top 250 rated movies from IMDB
def scrape_movies(limit: int = 250) -> list[dict]:
    response = requests.get(SCRAPE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('td.titleColumn')
    cast = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
               for b in soup.select('td.posterColumn span[name=ir]')]

    return __extract_movie_infos_to_list(limit, movies, cast, ratings)

# Transforms movie data into a list of dictionaries
def __extract_movie_infos_to_list(limit: int, movies, cast: list[str], ratings: list[str]) -> list[dict]:
    list = []
    for index in range(0, limit):
        movie_string = movies[index].get_text()
        movie = __format_movie_into_line(movie_string)

        id = index + 1
        title = __extract_title_from_movie(index, movie)
        year = __extract_year_from_movie(movie_string)
        rating = __format_rating(ratings[index])

        list.append(__movie_info_to_dict(id, title, year, rating, cast[index]))
    return list

def __movie_info_to_dict(id: int, title: str, year: str, rating: float, cast: str) -> dict:
    return {'id': id, 'title': title, 'year': year, 'ratings': rating, 'cast': cast}

def __format_movie_into_line(movie_string: str) -> str:
    return ' '.join(movie_string.split()).replace('.', '')

def __extract_title_from_movie(index: int, movie: str) -> str:
    return movie[len(str(index))+1:-7]

def __extract_year_from_movie(movie_string: str) -> str:
    return re.search('\((.*?)\)', movie_string).group(1)

def __format_rating(rating: str) -> float:
    return round(float(rating), 1)
