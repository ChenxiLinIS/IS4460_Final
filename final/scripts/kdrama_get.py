import requests
import json

id = 1 #kdramaID

#API endpoint for specific kdrama
api_url = f'http://localhost:8000/kdrama/kdrama/{id}/'

#GET request to retrieve kdrama
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
else:
    print("Error retrieving kdrama.")