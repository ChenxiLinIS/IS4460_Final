import requests
import json

id = 21 # characterID

#API endpoint for character
api_url = f'http://localhost:8000/kdrama/character/{id}/'

character_data = {
    "name": "test",
    "kdrama" : 22
}


#send PUT request to update character
response = requests.put(api_url, data=json.dumps(character_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Character updated successfully.")
else:
    print("Error updating character.")