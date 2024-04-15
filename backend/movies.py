from pydantic import BaseModel, Field
from typing import List, Set

class Movie(BaseModel):
    id: int
    name: str
    cast: List[str]

class Movies:
    def __init__(self, movies_file):
        self._movies = []
        self.counter = 1

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                elif row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                elif row_idx % 3 == 2:
                    movie_data = Movie(id=self.counter, name=movie_name, cast=movie_cast)
                    self._movies.append(movie_data.dict())
                    self.counter += 1
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'id': self.counter,
                    'name': movie_name,
                    'cast': movie_cast
                }
            )

    def list_movie_names(self):
        return [movie['name'] for movie in self._movies]

    def search_movies_by_name(self, keyword):
        keyword = keyword.lower()
        results = [movie['name'] for movie in self._movies if keyword in movie['name'].lower()]
        return results

    def search_movies_by_cast(self, keyword):
        keyword = keyword.lower()
        cast_list = []
        for movie in self._movies:
            movie_name = movie['name']
            cast = [actor for actor in movie['cast'] if keyword in actor.lower()]
            if cast:
                cast_list.append((movie_name, cast))
        return cast_list

    def add_movie_id(self, movie_id, new_id):
        for movie in self._movies:
            if movie['id'] == movie_id:
                movie['id'] = new_id
                break

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    for idx, name in enumerate(movies.list_movie_names(), start=1):
        print(f"{idx}. {name}")
    print(movies.search_movies_by_name('keyword'))

    for movie in movies._movies:
        print(movie["id"])
        print(movie["name"])

