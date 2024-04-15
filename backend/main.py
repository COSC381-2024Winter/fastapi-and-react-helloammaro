from fastapi import FastAPI, HTTPException
from typing import Union
from movies import Movies, Movie
from pydantic import BaseModel, Field

app = FastAPI()

movies = Movies('./movies.txt')

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



