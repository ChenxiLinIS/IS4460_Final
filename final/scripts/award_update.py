import requests
import json

id = 21 # awardID

#API endpoint for award
api_url = f'http://localhost:8000/kdrama/award/{id}/'

award_data = {
        "name": "test",
        "type": "test",
        "kdrama": 22
}


#send PUT request to update award
response = requests.put(api_url, data=json.dumps(award_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Award updated successfully.")
else:
    print("Error updating Award.")