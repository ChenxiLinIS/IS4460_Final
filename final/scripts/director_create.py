import json
import requests

# Define the URL of the API endpoint for creating directors
api_url = 'http://localhost:8000/kdrama/director/'

# Define director data along with the corresponding KDrama IDs
directors = [
    {
        "first_name": "Lee",
        "last_name": "Eung-bok",
        "kdrama": 1
    },
    {
        "first_name": "Kim",
        "last_name": "Jang-han",
        "kdrama": 2
    },
    {
        "first_name": "Lee",
        "last_name": "Jung-hyo",
        "kdrama": 3
    },
    {
        "first_name": "Kim",
        "last_name": "Seong-yoon",
        "kdrama": 4
    },
    {
        "first_name": "Kim",
        "last_name": "Hee-won",
        "kdrama": 5
    },
    {
        "first_name": "Shin",
        "last_name": "Won-ho",
        "kdrama": 6
    },
    {
        "first_name": "Jang",
        "last_name": "Tae-yoo",
        "kdrama": 7
    },
    {
        "first_name": "Myoungwoo",
        "last_name": "Lee",
        "kdrama": 8
    },
    {
        "first_name": "Kim",
        "last_name": "Won-suk",
        "kdrama": 9
    },
    {
        "first_name": "Im",
        "last_name": "Hyun-wook",
        "kdrama": 10
    },
    {
        "first_name": "Baek",
        "last_name": "Sang-hoon",
        "kdrama": 11
    },
    {
        "first_name": "Lee",
        "last_name": "Yoon-jung",
        "kdrama": 12
    },
    {
        "first_name": "Oh",
        "last_name": "Chung-hwan",
        "kdrama": 13
    },
    {
        "first_name": "Park",
        "last_name": "Seon-ho",
        "kdrama": 14
    },
    {
        "first_name": "Lee",
        "last_name": "Hyung-min",
        "kdrama": 15
    },
    {
        "first_name": "Kim",
        "last_name": "Kyu-tae",
        "kdrama": 16
    },
    {
        "first_name": "Jeon",
        "last_name": "Ki-sang",
        "kdrama": 17
    },
    {
        "first_name": "Choi",
        "last_name": "Sung-bum",
        "kdrama": 18
    },
    {
        "first_name": "Jung",
        "last_name": "Dae-yoon",
        "kdrama": 19
    },
    {
        "first_name": "Shin",
        "last_name": "Woo-chul",
        "kdrama": 20
    },
        {
        "first_name": "test",
        "last_name": "test",
        "kdrama": 22
    }
]

# Iterate over each director data and send a POST request for each one
for director_data in directors:
    response = requests.post(url=api_url, data=json.dumps(director_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Director '{director_data['first_name']} {director_data['last_name']}' created successfully.")
    else:
        print(f"Error creating director '{director_data['first_name']} {director_data['last_name']}': {response.content}")
