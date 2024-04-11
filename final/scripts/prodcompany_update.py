import requests
import json

id = 21 # prodcompanyID

#API endpoint for prodcompany
api_url = f'http://localhost:8000/kdrama/prod_company/{id}/'

prodcompany_data = {
        "name": "test",
        "year_founded": "test",
        "kdrama": 22
}


#send PUT request to update prod_company
response = requests.put(api_url, data=json.dumps(prodcompany_data), headers={'Content-Type' : 'application/json'})

#check response status code
if response.status_code == 200:
    print("Production company updated successfully.")
else:
    print("Error updating production company.")