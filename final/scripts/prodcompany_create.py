import json
import requests

# Define the URL of the API endpoint for creating production companies
api_url = 'http://localhost:8000/kdrama/prod_company/'

# Define production company data along with the corresponding KDrama IDs
production_companies = [
    {
        "name": "Next Entertainment World",
        "year_founded": "2008",
        "kdrama": 1
    },
    {
        "name": "Studio S",
        "year_founded": "2010",
        "kdrama": 2
    },
    {
        "name": "Culture Depot",
        "year_founded": "2010",
        "kdrama": 3
    },
    {
        "name": "Showbox",
        "year_founded": "1999",
        "kdrama": 4
    },
    {
        "name": "Logos Film",
        "year_founded": "2000",
        "kdrama": 5
    },
    {
        "name": "Egg is Coming",
        "year_founded": "2018",
        "kdrama": 6
    },
    {
        "name": "HB Entertainment",
        "year_founded": "2006",
        "kdrama": 7
    },
    {
        "name": "Taewon Entertainment",
        "year_founded": "1995",
        "kdrama": 8
    },
    {
        "name": "AStory",
        "year_founded": "2004",
        "kdrama": 9
    },
    {
        "name": "NPIO Entertainment",
        "year_founded": "2019",
        "kdrama": 10
    },
    {
        "name": "Studio Dragon",
        "year_founded": "2016",
        "kdrama": 11
    },
    {
        "name": "Kross Pictures",
        "year_founded": "2003",
        "kdrama": 12
    },
    {
        "name": "SidusHQ",
        "year_founded": "2001",
        "kdrama": 13
    },
    {
        "name": "Kakao Entertainment",
        "year_founded": "2021",
        "kdrama": 14
    },
    {
        "name": "Drama House",
        "year_founded": "1999",
        "kdrama": 15
    },
    {
        "name": "GT Entertainment",
        "year_founded": "2010",
        "kdrama": 16
    },
    {
        "name": "Group 8",
        "year_founded": "2000",
        "kdrama": 17
    },
    {
        "name": "Art & Culture",
        "year_founded": "2000",
        "kdrama": 18
    },
    {
        "name": "Chorokbaem Media",
        "year_founded": "2000",
        "kdrama": 19
    },
    {
        "name": "Hwa & Dam Pictures",
        "year_founded": "2007",
        "kdrama": 20
    },
        {
        "name": "test",
        "year_founded": "test",
        "kdrama": 22
    }
]

# Iterate over each production company data and send a POST request for each one
for company_data in production_companies:
    response = requests.post(url=api_url, data=json.dumps(company_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Production company '{company_data['name']}' created successfully.")
    else:
        print(f"Error creating production company '{company_data['name']}': {response.content}")
