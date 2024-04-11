import requests
import json

id = 1 #awawrdID

#API endpoint for specific award
api_url = f'http://localhost:8000/kdrama/award/{id}/'

#GET request to retrieve award
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    award_data = response.json()
    print(award_data)
else:
    print("Error retrieving award.")