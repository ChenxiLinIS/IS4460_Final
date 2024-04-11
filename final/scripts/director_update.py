import requests
import json

id = 21 # directorID

#API endpoint for director
api_url = f'http://localhost:8000/kdrama/director/{id}/'

director_data = {
        "first_name": "test",
        "last_name": "test",
        "kdrama": 22
}


#send PUT request to update director
response = requests.put(api_url, data=json.dumps(director_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Director updated successfully.")
else:
    print("Error updating Director.")