import requests
import json

id = 1 #characterID

#API endpoint for specific character
api_url = f'http://localhost:8000/kdrama/character/{id}/'

#GET request to retrieve character
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    character_data = response.json()
    print(character_data)
else:
    print("Error retrieving character.")