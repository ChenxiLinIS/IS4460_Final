import requests
import json

id = 1 #prodcompanyID

#API endpoint for specific production company
api_url = f'http://localhost:8000/kdrama/prod_company/{id}/'

#GET request to retrieve production company
response = requests.get(api_url)

#check response status code
if response.status_code == 200:
    prodcompany_data = response.json()
    print(prodcompany_data)
else:
    print("Error retrieving production company.")