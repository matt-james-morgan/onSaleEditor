import requests
import json
from constants import API_KEY, CLIENT_ID



url = "https://cloud.lightspeedapp.com/oauth/authorize.php?response_type=code&client_id={BATEMAN_CLIENT_ID}&scope=employee:inventory_read"



response = requests.request("GET", url)

print(response)


accessToken = 'https://cloud.lightspeedapp.com/oauth/authorize.php?response_type=code&client_id={BATEMAN_CLIENT_ID}&scope=employee:inventory_read'


accessTokenResponse = requests(accessToken)

if accessTokenResponse.status_code == 200:
    data = response
    print(data)
else:
    print('Error:', response.status_code)

# def get_access_token(url, client_id, client_secret):
#     response = requests.post(
#         url,
#         data={"grant_type": "client_credentials"},
#         auth=(client_id, client_secret),
#     )
#     return response.json()["access_token"]