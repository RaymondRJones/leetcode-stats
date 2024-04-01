# Welcome to Twitch Stats 2024

I made this to just show some of the twitch streamers and community members stats. It's just a basic JSON that displays all their ratings with their LC profiles.

# To Make Improvements

The project is pure react React

Node version is `v20.5.1`


### To run:

git clone the repo

cd into `leetcode-elo` like

```
cd leetcode-elo
```

Make sure you ran `npm install` beforehand

```
  npm start
```

You should see the homepage which loads the leaderboard.


### Main Files

99% of logic is `src/components/leaderboard.js`

This displays the leaderboard and imports data from a json that contains all user profiles and elo, hardcoded values.

## Ideas for Improvement

There are two core ideas

### Idea 1

Instead of the function

`fetchLeader()` importing a hardcoded JSON
 
 We can create a new function that will pull data from an AWS S3 bucket (Or Google Drive or whatever) an updated file. 

The benefit is that this is easier for anyone to update (And even a server can perform the updates themselves)

```Javascript
// line 21
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
```

### Idea 2

Write an AWS Lambda function (Or run a server), that periodically grabs data from 

`leetcode.com` (For true ratings)
`https://lccn.lbao.site/predicted/weekly-contest-388` (For estimated ratings)

Idk anything about the lccn website or API. But for Leetcode, I wrote a function and tested it. It works assuming you pass in valid cookies and make the request look like a human. 

You could add a for loop for every leetcoder and update their JSON values and then put the JSON into the cloud or CDN to be pulled from any leaderboard react app.

```python
def get_elo_of_leetcoder(username):

url = "https://leetcode.com/graphql"

	payload = {
	
		"operationName": "userContestRankingInfo",
		
		"query": """
		
		query userContestRankingInfo($username: String!) {
		
		userContestRanking(username: $username) {
		
		rating

	}

}

""",

"variables": {

"username": username

}

}

	response = requests.post(url, headers=headers, cookies=cookies, json=payload)
	
	if response.status_code == 200:
	
		data = response.json()

	# Extract the rating from the response
	
	rating = data['data']['userContestRanking']['rating']
	
	return rating
	
	else:
	
	# Handle errors
	
	print('Failed to retrieve data:', response.status_code)
	
	print('Response:', response.text)

return None
```


### Bonus Stuff

The favicon in public still has the react symbol on it.

Anything else you want to add?





