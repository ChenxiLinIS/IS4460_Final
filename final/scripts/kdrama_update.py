import requests
import json

id = 21 # kdramaID

#API endpoint for kdrama
api_url = f'http://localhost:8000/kdrama/kdrama/{id}/'

kdrama_data = {
        "title": "Kdrama Test 1",
        "description": "Test 1.",
        "release_year": "Test 1.",
        "duration": "Test episodes"
}


#send PUT request to update kdrama
response = requests.put(api_url, data=json.dumps(kdrama_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Kdrama updated successfully.")
else:
    print("Error updating Kdrama.")