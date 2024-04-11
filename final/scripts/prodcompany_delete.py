import requests
import json

id = 21 #prodcompanyID

#API endpoint for specific prod company
api_url = f'http://localhost:8000/kdrama/prod_company/{id}/'

#DELETE request to retrieve prod copmany
response = requests.delete(api_url)

#check response status code
if response.status_code == 204:
    print("Production company deleted successfully.")
else:
    print("Error deleting production company.")