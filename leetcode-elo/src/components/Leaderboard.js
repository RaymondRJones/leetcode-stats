import React, { useState, useEffect } from 'react';
import { Container, Typography, List, ListItem, ListItemAvatar, Avatar, Grid, Box, CircularProgress, TextField, CardActionArea } from '@mui/material';
import { styled } from '@mui/material/styles';

const CustomCard = styled(Box)(({ theme }) => ({
  marginBottom: theme.spacing(2),
  borderRadius: theme.shape.borderRadius,
  boxShadow: '0 4px 20px rgba(0,0,0,0.1)',
  transition: '0.3s',
  '&:hover': {
    transform: 'scale(1.02)',
    boxShadow: '0 6px 24px rgba(0,0,0,0.15)',
  },
}));

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const response = await fetch('/users_by_elo.json');
      const data = await response.json();
      data.sort((a, b) => b.elo - a.elo);
      setLeaderboard(data);
      setLoading(false);
    };

    fetchLeaderboard();
  }, []);

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <CircularProgress />
      </Box>
    );
  }

  const handleCardClick = (profileName) => {
    window.open(`https://leetcode.com/${profileName}`, '_blank');
  };

  // Function to filter leaderboard based on search term
  const filteredLeaderboard = searchTerm
    ? leaderboard.filter((user) =>
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        `${user.rank}`.startsWith(searchTerm) // Assuming rank is a property you have or can compute
      )
    : leaderboard;

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom component="div" sx={{ fontFamily: "'Roboto', sans-serif", fontWeight: 500 }}>
        2024 Twitch Leetcode Leaderboard
      </Typography>
      <Typography variant="h6" gutterBottom component="div" sx={{ fontFamily: "'Roboto', sans-serif", fontWeight: 500 }}>
        (Updated March 24th, 2024)
      </Typography>
      <TextField
        fullWidth
        label="Search by name"
        variant="outlined"
        sx={{ mb: 2 }}
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
        {filteredLeaderboard.map((user, index) => (
          <CustomCard key={index}>
            <CardActionArea onClick={() => handleCardClick(user.name)}>
              <ListItem alignItems="flex-start">
                <Grid container justifyContent="space-between" alignItems="center">
                  <Grid item>
                    <Typography variant="h6" component="span" sx={{ fontFamily: "'Roboto', sans-serif" }}>
                      #{index + 1} {user.name}
                    </Typography>
                  </Grid>
                  <Grid item>
                    <Typography variant="subtitle1" component="span" sx={{ fontWeight: 'bold', fontFamily: "'Roboto', sans-serif" }}>
                      ELO: {user.elo}
                    </Typography>
                  </Grid>
                </Grid>
              </ListItem>
            </CardActionArea>
          </CustomCard>
        ))}
      </List>
    </Container>
  );
}

export default Leaderboard;
