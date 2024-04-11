import requests
import json

id = 21 #awardID

#API endpoint for specific award
api_url = f'http://localhost:8000/kdrama/award/{id}/'

#DELETE request to retrieve award
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Award deleted successfully.")
else:
    print("Error deleting Award.")