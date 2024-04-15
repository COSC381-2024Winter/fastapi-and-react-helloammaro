import './App.css';
import { useEffect, useState } from 'react';
import { TextField, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import LocalMoviesIcon from '@mui/icons-material/LocalMovies';

function App() {
  const [movieId, setMovieId] = useState("1");
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    if (movieId === "") {
      setMovie(null);
    } else {
      fetch(`http://localhost:8000/movies/${movieId}`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Movie not found');
          }
          return response.json();
        })
        .then(result => {
          setMovie(result);
        })
        .catch(error => {
          console.error('Error fetching movie:', error);
          setMovie(null);
        });

    }
  }, [movieId]);

  useEffect(() => {
    console.log(movie);
    }
  , [movie]);


  return (
    <div className="App">
      <header className="App-header">
        <TextField
          id="outlined-basic"
          label="MovieId"
          variant="outlined"
          color="success"
          value={movieId}
          onChange={e => setMovieId(e.target.value)}
        />
      </header>
    </div>
  );
}

export default App;

