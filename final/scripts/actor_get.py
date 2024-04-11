import requests
import json

id = 1 #actorID

#API endpoint for specific actor
api_url = f'http://localhost:8000/kdrama/actor/{id}/'

#GET request to retrieve actor
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    actor_data = response.json()
    print(actor_data)
else:
    print("Error retrieving actor.")