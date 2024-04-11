import requests
import json

id = 21 # actorID

#API endpoint for actor
api_url = f'http://localhost:8000/kdrama/actor/{id}/'

actor_data = {
        "first_name": "test",
        "last_name": "test",
        "birth_date": "1978-06-28",
        "character": 21
}


#send PUT request to update actor
response = requests.put(api_url, data=json.dumps(actor_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Actor updated successfully.")
else:
    print("Error updating Actor.")