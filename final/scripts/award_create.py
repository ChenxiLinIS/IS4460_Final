import json
import requests

# Define the URL of the API endpoint for creating awards
api_url = 'http://localhost:8000/kdrama/award/'

# Define award data along with the corresponding KDrama IDs
awards = [
    {
        "name": "Rookie Asia Awards",
        "type": "Male Rookie of the Year",
        "kdrama": 1
    },
    {
        "name": "2023 SBS Drama Awards",
        "type": "Best Couple",
        "kdrama": 2
    },
    {
        "name": "Seoul International Drama Awards",
        "type": "Outstanding Korean Actress",
        "kdrama": 3
    },
    {
        "name": "Baeksang Arts Awards",
        "type": "Best New Actress",
        "kdrama": 4
    },
    {
        "name": "Brand of the Year Awards",
        "type": "Drama of the Year",
        "kdrama": 5
    },
    {
        "name": "Asian Artist Awards",
        "type": "AAA Focus Award",
        "kdrama": 6
    },
    {
        "name": "Shanghai Television Festival Magnolia Awards",
        "type": "Silver Award, Best Foreign TV Series",
        "kdrama": 7
    },
    {
        "name": "APAN Star Awards",
        "type": "Best Supporting Actress",
        "kdrama": 8
    },
    {
        "name": "tvN10 Awards",
        "type": "PD's Choice Award",
        "kdrama": 9
    },
    {
        "name": "Fundex Awards",
        "type": "Grand Prize (Daesang)",
        "kdrama": 10
    },
    {
        "name": "2020 SBS Drama Awards",
        "type": "Top Excellence Award",
        "kdrama": 11
    },
    {
        "name": "Korean Cable TV Awards 2016",
        "type": "Best Actor",
        "kdrama": 12
    },
    {
        "name": "Korea First Brand Awards",
        "type": "Drama Category",
        "kdrama": 13
    },
    {
        "name": "Korea Drama Awards",
        "type": "Best New Actress",
        "kdrama": 14
    },
    {
        "name": "Seoul International Drama Awards",
        "type": "Outstanding Korean Actress",
        "kdrama": 15
    },
    {
        "name": "Drama Fever Awards",
        "type": "Best Historical Drama",
        "kdrama": 16
    },
    {
        "name": "Korean Junior Star Awards",
        "type": "Best New Actor in a TV Drama",
        "kdrama": 17
    },
    {
        "name": "Soompi Awards",
        "type": "Best New Actor",
        "kdrama": 18
    },
    {
        "name": "MBC Drama Awards",
        "type": "Drama of the Year",
        "kdrama": 19
    },
    {
        "name": "Grimae Awards",
        "type": "Grand Prize",
        "kdrama": 20
    },
        {
        "name": "test",
        "type": "test",
        "kdrama": 22
    }
]

# Iterate over each award data and send a POST request for each one
for award_data in awards:
    response = requests.post(url=api_url, data=json.dumps(award_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Award '{award_data['name']}' created successfully.")
    else:
        print(f"Error creating award '{award_data['name']}': {response.content}")
