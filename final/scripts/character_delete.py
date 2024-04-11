import requests
import json

id = 21 #characterID

#API endpoint for specific character
api_url = f'http://localhost:8000/kdrama/character/{id}/'

#DELETE request to retrieve character
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Character deleted successfully.")
else:
    print("Error deleting character.")