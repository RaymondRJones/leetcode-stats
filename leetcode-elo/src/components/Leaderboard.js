import React, { useState, useEffect } from 'react';
import { Container, Typography, List, ListItem, ListItemAvatar, Avatar, ListItemText, Card, Grid } from '@mui/material';
import SportsEsportsIcon from '@mui/icons-material/SportsEsports'; // Example icon

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const response = await fetch('/leaderboard.json');
      const data = await response.json();
      data.sort((a, b) => b.elo - a.elo);
      setLeaderboard(data);
    };

    fetchLeaderboard();
  }, []);

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom component="div">
        Twitch 2024 Leaderboard
      </Typography>
      <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
        {leaderboard.map((user, index) => (
          <Card key={index} sx={{ mb: 2, boxShadow: 3 }}>
            <ListItem alignItems="flex-start">
              <ListItemAvatar>
              </ListItemAvatar>
              <Grid container justifyContent="space-between" alignItems="center">
                <Grid item>
                  <Typography variant="h6" component="span">
                    #{index + 1} {user.name}
                  </Typography>
                </Grid>
                <Grid item>
                  <Typography variant="subtitle1" component="span" sx={{ fontWeight: 'bold' }}>
                    ELO: {user.elo}
                  </Typography>
                </Grid>
              </Grid>
            </ListItem>
          </Card>
        ))}
      </List>
    </Container>
  );
}

export default Leaderboard;
