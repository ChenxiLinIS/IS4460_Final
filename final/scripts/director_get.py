import requests
import json

id = 1 #directorID

#API endpoint for specific director
api_url = f'http://localhost:8000/kdrama/director/{id}/'

#GET request to retrieve director
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    director_data = response.json()
    print(director_data)
else:
    print("Error retrieving director.")