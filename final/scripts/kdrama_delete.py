import requests
import json

id = 22 #kdramaID

#API endpoint for specific Kdrama
api_url = f'http://localhost:8000/kdrama/kdrama/{id}/'

#DELETE request to retrieve kdrama
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Kdrama deleted successfully.")
else:
    print("Error deleting Kdrama.")