import React, { useState, useEffect } from 'react';
import { Container, Typography, List, ListItem, ListItemAvatar, Avatar, Grid, Box, CircularProgress, CardActionArea } from '@mui/material';
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

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const response = await fetch('/leaderboard.json');
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

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom component="div" sx={{ fontFamily: "'Roboto', sans-serif", fontWeight: 500 }}>
        Community Leaderboard 2024
      </Typography>
      <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
        {leaderboard.map((user, index) => (
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
