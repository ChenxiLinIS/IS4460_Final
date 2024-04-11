import requests
import json

id = 21 #actorID

#API endpoint for specific actor
api_url = f'http://localhost:8000/kdrama/actor/{id}/'

#DELETE request to retrieve movie
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Actor deleted successfully.")
else:
    print("Error deleting Actor.")