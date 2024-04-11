import json
import requests

# Define the URL of the API endpoint for creating characters
api_url = 'http://localhost:8000/kdrama/character/'

# Define character data along with the corresponding KDrama IDs

characters = [
    {"name": "Yoo Shi-jin", "kdrama": 1},
    {"name": "Jeong Gu-Won", "kdrama": 2},
    {"name": "Yoon Se-ri", "kdrama": 3},
    {"name": "Park Saeroyi", "kdrama": 4},
    {"name": "Vincenzo Cassano", "kdrama": 5},
    {"name": "Ahn Jeong-won", "kdrama": 6},
    {"name": "Cheon Song-yi", "kdrama": 7},
    {"name": "Jung Saet-byul", "kdrama": 8},
    {"name": "Park Hae-young", "kdrama": 9},
    {"name": "Cheon Sa-rang", "kdrama": 10},
    {"name": "Lee Gon", "kdrama": 11},
    {"name": "Hong Seol", "kdrama": 12},
    {"name": "Nam Hong-joo", "kdrama": 13},
    {"name": "Kang Tae-moo", "kdrama": 14},
    {"name": "Do Bong-soon", "kdrama": 15},
    {"name": "Hae Soo", "kdrama": 16},
    {"name": "Geym Jan-di", "kdrama": 17},
    {"name": "Kang Mi-rae", "kdrama": 18},
    {"name": "Oh Yeon-joo", "kdrama": 19},
    {"name": "Gil Ra-im", "kdrama": 20},
    {"name": "test","kdrama" :22}
]

# Iterate over each character data and send a POST request for each one
for character_data in characters:
    response = requests.post(url=api_url, data=json.dumps(character_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Character '{character_data['name']}' created successfully.")
    else:
        print(f"Error creating character '{character_data['name']}': {response.content}")
