import requests
import json

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
}

def get_delta_rating_of_user(username, contest_name):
    url = f"https://lccn.lbao.site/api/v1/contest-records/user?contest_name={contest_name}&username={username}&archived=false"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0].get('delta_rating')
    print('Failed to retrieve data for {}: {}'.format(username, response.status_code))
    print("They probably didn't take the contest...")
    return None

def load_existing_elos(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def update_elos_with_new_ratings(existing_elos, user_ratings):
    elo_dict = {user['name']: user for user in existing_elos}
    for username, delta in user_ratings:
        if username in elo_dict:
            elo_dict[username]['elo'] += delta
    return list(elo_dict.values())

def write_elos_to_json(filename, updated_elos):
    with open(filename, 'w') as file:
        json.dump(updated_elos, file, indent=4)

def main():
    existing_elos = load_existing_elos('../leetcode-elo/public/users_by_elo.json')
    usernames = [user['name'] for user in existing_elos]
    user_ratings = []
    for username in usernames:
        print("Getting delta rating of...", username)
        delta_rating = get_delta_rating_of_user(username, "weekly-contest-388")
        if delta_rating is not None:
            delta = int(delta_rating)
            user_ratings.append((username, delta))
            print("Success! Adding delta rating", delta, "to", username)
    updated_elos = update_elos_with_new_ratings(existing_elos, user_ratings)
    write_elos_to_json('../leetcode-elo/public/users_by_elo.json', updated_elos)

if __name__ == "__main__":
    main()

