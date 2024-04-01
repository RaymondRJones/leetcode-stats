const AWS = require('aws-sdk');
const https = require('https');

// Set the AWS Region
AWS.config.update({region: 'us-east-1'}); // Update this to your region

// Create the DynamoDB service object
const ddb = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    // Define the start and end pagination
    const startPagination = 1;
    const endPagination = 1000;
    const contestName = 'weekly-contest-388'; // Update as necessary
    
    for (let pagination = startPagination; pagination <= endPagination; pagination++) {
        const data = await getContestData(contestName, pagination);
        
        // Break if there are no users in the current pagination
        if (!data.total_rank.length) {
            break;
        }
        
        for (let user of data.total_rank) {
            const username = user.username;
            const problemsSolved = {};
            data.questions.forEach(question => {
                problemsSolved[question.question_id] = 0; // Initialize problem solved count
            });

            // Assuming 'data.submissions' is structured as per your needs
            data.submissions.forEach(submission => {
                Object.values(submission).forEach(detail => {
                    if (detail.status === 10) { // Check if the problem was solved
                        problemsSolved[detail.question_id]++;
                    }
                });
            });

            await ddb.put({
                TableName: 'LeetCodeContest',
                Item: {
                    'ContestName': contestName,
                    'Username': username,
                    'ProblemsSolved': problemsSolved
                }
            }).promise();
        }
    }

    return {
        statusCode: 200,
        body: 'Data successfully saved to DynamoDB',
    };
};

function getContestData(contestName, pagination) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'leetcode.com',
            path: `/contest/api/ranking/${contestName}/?pagination=${pagination}&region=global`,
            method: 'GET',
        };
        
        const req = https.request(options, (res) => {
            let data = '';
            
            res.on('data', (chunk) => {
                data += chunk;
            });
            
            res.on('end', () => {
                resolve(JSON.parse(data));
            });
        });
        
        req.on('error', (e) => {
            reject(e);
        });
        
        req.end();
    });
}
