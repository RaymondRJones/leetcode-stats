import requests
import sqlite3
import json

# Database setup
conn = sqlite3.connect('leetcode_contest.db')
cursor = conn.cursor()
# This time, create a new table specifically for tracking problem solvers
"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProblemSolvers (
    ContestName TEXT,
    QuestionID INTEGER,
    Username TEXT,
    PRIMARY KEY (ContestName, QuestionID, Username)
)
''')
conn.commit()
"""
cookies = {
    "__cf_bm": "HVV6_vLLqqRXtACO9lMtOdp_z_CaQEBFL6WiY5ix4UA-1710343407-1.0.1.1-xsU8nMH6e200iQ6Ndpgx5iZfgxlFUp5IXwcMPOHIJBsrbtj_aqB5JiAWGn2oASQrSiAeD1p8eR6C5MlDguOCZA",
    "__stripe_mid": "a80e1a68-7d69-4861-93d6-94410de982beda7d04",
    "_dd_s": "rum=0&expire=1710344635795",
    "_ga": "GA1.2.952786075.1680444489",
    "_ga_CDRWKZTDEX": "GS1.1.1680984327.14.1.1680986369.0.0.0",
    "87b5a3c3f1a55520_gr_cs1": "ItsRaymond",
    "87b5a3c3f1a55520_gr_last_sent_cs1": "ItsRaymond",
    "cf_clearance": "zhrl8tJD6BG66Lc72rJbEp6eLhbAB4vC9OmBfbCI7_w-1710341535-1.0.1.1-BH3GkfEiYSH6J9XTM57QNU2f8bbcnweJ3gVSp9gW7sAgFxu_9zehe3zozjNh8OlYoSdzXmghw7j.V9aNp3e2RA",
    "csrftoken": "I2pNSdoqVI5nVWt7iFqDfeqH0MQN7vDz47VKC7KQFf10Qi7kSyi4s427w6lc7gvX",
    "gr_user_id": "ce2b8790-e558-4331-a8fe-6ef19c1a6c48",
    "INGRESSCOOKIE": "0921facb932289ee856a751843282fac|8e0876c7c1464cc0ac96bc2edceabd27",
    "LEETCODE_SESSION": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTE2MzE0NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImU2OWFhMWM2MWE5YzhiNDZhNmI0OThhNzFiY2M2NTg3NWNiYjI5M2FjZjc1YmZkZGE3NWU4NThjNTI5ZTRiODEiLCJpZCI6MTE2MzE0NCwiZW1haWwiOiJkYXJrbW9vbmtuaWdodF8yQGhvdG1haWwuY29tIiwidXNlcm5hbWUiOiJJdHNSYXltb25kIiwidXNlcl9zbHVnIjoiSXRzUmF5bW9uZCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNzAwMTYxOTY2LnBuZyIsInJlZnJlc2hlZF9hdCI6MTcxMDI5NjkzMywiaXAiOiIxODEuNTguMTM4LjE3OCIsImlkZW50aXR5IjoiZTE3ODlkMzVhNmQ2ZTdmNmFkNDNiNDZlOGI3ZDRjNDMiLCJzZXNzaW9uX2lkIjo0NzY5NjM1NiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.usnZWWRTRLDPPskL_oEBESBFmTB8sfILYXrGYntjvuc"
    # Add all other cookies here
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
}

def get_contest_data(contest_name, pagination):
    url = 'https://leetcode.com/contest/api/ranking/' + contest_name + '/?pagination=' + str(pagination) + '&region=global'
    print("Requesting from Leetcode", url)

    response = requests.get(url, headers=headers, cookies=cookies)
    print('Response status code:', response.status_code)  # Print out the status code
    try:
        response.raise_for_status()  # This will raise an exception for 4XX/5XX errors
        return response.json()
    except requests.exceptions.HTTPError as e:
        # If a HTTP error occurs, print out the error and the response content
        print('HTTP Error:', e)
        print('Response content:', response.text)  # This will print the response content that led to the error
        raise  

def store_data(contest_name, username, problems_solved):
    print("storing data..")
    for question_id, solved in problems_solved.items():
        if solved:
            cursor.execute('''
            INSERT INTO ProblemSolvers (ContestName, QuestionID, Username)
            VALUES (?, ?, ?)
            ''', (contest_name, question_id, username))
    conn.commit()


def get_results_from_lc(start, end):
    start_pagination = start
    end_pagination = end  # Adjust based on the actual number of pages
    contest_name = 'weekly-contest-388'  # Update as necessary
    
    for pagination in range(start_pagination, end_pagination + 1):

        data = get_contest_data(contest_name, pagination)

        if not data.get('total_rank'):
            print('No more data available after page', pagination)
            break
        
        for i, user in enumerate(data['total_rank']):
            username = user['username']

            problems_solved = {str(question['question_id']): False for question in data['questions']}
            user_submissions = data['submissions'][i] if i < len(data['submissions']) else {}

            for question_id, submission_details in user_submissions.items():

                if submission_details.get('status') == 10:  # Status 10 means solved
                    problems_solved[str(question_id)] = True

            store_data(contest_name, username, problems_solved)

        print('Page', pagination, 'processed')

    conn.close()
    print('All data processed successfully')

# i.e question_id 3334
def get_solvers_of_question(question_id):
    # Replace '3334' with the actual QuestionID for question 1
    cursor.execute('SELECT Username FROM ProblemSolvers WHERE QuestionID = ?', (question_id,))
    solvers = cursor.fetchall()  # Fetch all results
    usernames = [solver[0] for solver in solvers]  # Extract usernames from the query results
    return usernames

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

def update_elo(elo_user, elo_problem, user_solved):
    K = 32  # Change this based on your desired volatility
    actual_score_user = 1 if user_solved else 0
    actual_score_problem = 0 if user_solved else 1
    
    E_user = 1 / (1 + 10 ** ((elo_problem - elo_user) / 400))
    E_problem = 1 / (1 + 10 ** ((elo_user - elo_problem) / 400))
    
    new_elo_user = elo_user + K * (actual_score_user - E_user)
    new_elo_problem = elo_problem + K * (actual_score_problem - E_problem)
    
    return new_elo_user, new_elo_problem

# Basic ELO calculations based on PASS or FAIL
def calculate_elo_of_problem(user, question_id):
    all_users_who_solved_problem = []
    all_users_who_failed_problem = []
    problem_elo = 1500

    for user in all_users_who_solved_problem:
        elo_of_user = get_elo_of_leetcoder(user)
        user_res, problem_res = update_elo(elo_of_user, problem_elo, True)
        problem_elo = problem_res

    for user in all_users_who_failed_problem:
        elo_of_user = get_elo_of_leetcoder(user)
        user_res, problem_res = update_elo(elo_of_user, problem_elo, False)
        problem_elo = problem_res
    return problem_elo
def main():
    # get_results_from_lc(1,1)
    users = get_solvers_of_question(3334)
    

if __name__ == '__main__':
    main()
