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
      console.log(movieId);
    }
  }, [movieId]);

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
        <List>
          {movie && (
            <ListItem>
              <ListItemIcon>
                <LocalMoviesIcon />
              </ListItemIcon>
              <ListItemText primary={movie.name} />
            </ListItem>
          )}
        </List>
      </header>
    </div>
  );
}

export default App;

