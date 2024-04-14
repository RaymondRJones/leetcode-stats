#!/bin/bash


# Run the Python script
python query_users_elo_daily.py

# Navigate to the Git repository root
cd /Users/raymondjones/Documents/GitHub/leetcode-stats

# Git operations
git add leetcode-elo/public/*.json
git commit -m "Automated update of leaderboard"
git push origin main

