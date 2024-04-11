import json
import requests

# Define the URL of the API endpoint for creating actors
api_url = 'http://localhost:8000/kdrama/actor/'

# Define actor data along with the corresponding character foreign keys
actors = [
    {
        "first_name": "Song",
        "last_name": "Joong-ki",
        "birth_date": "1985-09-19",
        "character": 1
    },
    {
        "first_name": "Song",
        "last_name": "Kang",
        "birth_date": "1994-04-23",
        "character": 2
    },
    {
        "first_name": "Son",
        "last_name": "Ye-jin",
        "birth_date": "1982-01-11",
        "character": 3
    },
    {
        "first_name": "Park",
        "last_name": "Seo-joon",
        "birth_date": "1988-12-16",
        "character": 4
    },
    {
        "first_name": "Song",
        "last_name": "Joong-ki",
        "birth_date": "1985-09-19",
        "character": 5
    },
    {
        "first_name": "Yoo",
        "last_name": "Yeon-seok",
        "birth_date": "1984-04-11",
        "character": 6
    },
    {
        "first_name": "Jun",
        "last_name": "Ji-hyun",
        "birth_date": "1981-10-30",
        "character": 7
    },
    {
        "first_name": "Kim",
        "last_name": "Yoo-jung",
        "birth_date": "1999-09-22",
        "character": 8
    },
    {
        "first_name": "Lee",
        "last_name": "Je-hoon",
        "birth_date": "1984-07-04",
        "character": 9
    },
    {
        "first_name": "Im",
        "last_name": "Yoon-ah",
        "birth_date": "1990-05-30",
        "character": 10
    },
    {
        "first_name": "Lee",
        "last_name": "Min-ho",
        "birth_date": "1987-06-22",
        "character": 11
    },
    {
        "first_name": "Kim",
        "last_name": "Go-eun",
        "birth_date": "1991-07-02",
        "character": 12
    },
    {
        "first_name": "Lee",
        "last_name": "Jong-suk",
        "birth_date": "1989-09-14",
        "character": 13
    },
    {
        "first_name": "Ahn",
        "last_name": "Hyo-seop",
        "birth_date": "1995-04-17",
        "character": 14
    },
    {
        "first_name": "Park",
        "last_name": "Bo-young",
        "birth_date": "1990-02-12",
        "character": 15
    },
    {
        "first_name": "Lee",
        "last_name": "Ji-eun",
        "birth_date": "1993-05-16",
        "character": 16
    },
    {
        "first_name": "Koo",
        "last_name": "Hye-sun",
        "birth_date": "1984-11-09",
        "character": 17
    },
    {
        "first_name": "Im",
        "last_name": "Soo-hyang",
        "birth_date": "1990-04-19",
        "character": 18
    },
    {
        "first_name": "Han",
        "last_name": "Hyo-joo",
        "birth_date": "1987-02-22",
        "character": 19
    },
    {
        "first_name": "Ha",
        "last_name": "Ji-won",
        "birth_date": "1978-06-28",
        "character": 20
    },
    {
        "first_name": "test",
        "last_name": "test",
        "birth_date": "1978-06-28",
        "character": 21
    }
]

# Iterate over each actor data and send a POST request for each one
for actor_data in actors:
    response = requests.post(url=api_url, data=json.dumps(actor_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Actor '{actor_data['first_name']} {actor_data['last_name']}' created successfully.")
    else:
        print(f"Error creating actor '{actor_data['first_name']} {actor_data['last_name']}': {response.content}")
