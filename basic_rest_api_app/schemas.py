from pydantic import BaseModel

# Schema to have common attributes while creating or reading data.
class MovieBase(BaseModel):
    title: str
    year: int | None = None
    is_adult: bool
    runtime_minutes: int
    genres: str

# And create class that inherits from it, plus any additional data (attributes) needed for creation.
class MovieCreate(MovieBase):
    pass

# You can also add other attributes, like a list of genres. (maybe TODO)
# Move ID and other things inside DB here instead of MovieBase?
class Movie(MovieBase):
    id: str

    class Config:
        orm_mode = True
