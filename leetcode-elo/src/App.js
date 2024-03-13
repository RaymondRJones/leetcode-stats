import React from 'react';
import { AppBar, Toolbar, Typography, Container, TextField, Button, Box } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import DonateButton from './components/DonateButton';
function App() {
  const handleSearch = (event) => {
    // Implement the logic to search for LeetCode problems
    console.log(event.target.value);
  };

  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            LeetCode Elo
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="md">
        <Box my={4}>
          <Typography variant="h4" component="h1" gutterBottom>
            Find LeetCode Problems
          </Typography>
          <TextField
            fullWidth
            id="search-bar"
            label="Search for problems"
            variant="outlined"
            InputProps={{
              endAdornment: <SearchIcon />,
            }}
            onKeyPress={(ev) => {
              if (ev.key === 'Enter') {
                handleSearch(ev);
                ev.preventDefault();
              }
            }}
          />
        </Box>
      </Container>
      <Box mt={5} display="flex" justifyContent="center">
        <DonateButton></DonateButton>
      </Box>
    </div>
  );
}

export default App;