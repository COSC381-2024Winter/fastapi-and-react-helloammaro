from fastapi import FastAPI, HTTPException
from typing import Union
from movies import Movies, Movie
from pydantic import BaseModel, Field

app = FastAPI()

movies = Movies('./movies.txt')

class MovieRequest(BaseModel):
    movie_name: str
    movie_cast: list[str]


@app.get("/")
def welcome():
    return "Hello"

# get
@app.get("/movies/{movie_id}", response_model=Movie)
def find_movie_by_id(movie_id: int) -> Union[Movie, None]:
    for movie in movies._movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, new_movie: MovieRequest) -> Union[Movie, None]:
    for movie in movies._movies:
        if movie['id'] == movie_id:
            movie['name'] = new_movie.movie_name
            movie['cast'] = new_movie.movie_cast
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}", response_model=Movie)
def delete_movie(movie_id: int) -> Union[Movie, None]:
    for idx, movie in enumerate(movies._movies):
        if movie['id'] == movie_id:
            deleted_movie = movies._movies.pop(idx)
            return deleted_movie
    raise HTTPException(status_code=404, detail="Movie not found")




