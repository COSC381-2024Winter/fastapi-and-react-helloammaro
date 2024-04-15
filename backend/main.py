from fastapi import FastAPI, HTTPException
from typing import Union
from movies import Movies, Movie
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/movies", response_model=Movie)
def add_movie(added_movie: MovieRequest) -> Union[Movie, None]:
    new_id = (movies.counter) + 1
    new_movie = {
        'id': new_id,
        'name': added_movie.movie_name,
        'cast': added_movie.movie_cast
    }
    movies._movies.append(new_movie)
    movies.counter += 1
    return new_movie



