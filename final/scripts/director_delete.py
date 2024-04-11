import requests
import json

id = 21 #directorID

#API endpoint for specific director
api_url = f'http://localhost:8000/kdrama/director/{id}/'

#DELETE request to retrieve director
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Director deleted successfully.")
else:
    print("Error deleting director.")