import clientInfo
import genToken
import requests
import json

token = genToken.generateToken()

url = 'https://apx.cisco.com/cs/api/v1/collections/import-inventory'

params = {
    "customerId": clientInfo.CUSTOMER_ID,
    "inventoryName": clientInfo.INVENTORY_NAME
}

headers={
    "Authorization":"Bearer "+token
}

with open('inventory.json') as file:
    payload=json.load(file)
    file.close()

res = requests.post(url, params=params, json=payload, headers=headers)

try:
    print(res.json())
except Exception as e:
    print('An error has occured: ', e)

