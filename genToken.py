#This module generates an authentication token for SNTC collections
import requests, json
import clientInfo

url = 'https://cloudsso.cisco.com/as/token.oauth2'

id = clientInfo.CLIENT_ID
secret = clientInfo.CLIENT_SECRET


body = {
    'grant_type': 'client_credentials',
    'client_id' : id,
    'client_secret': secret
}

def generateToken():
    r = requests.post(url, data=body).json()
    token = r['access_token']
    return token

