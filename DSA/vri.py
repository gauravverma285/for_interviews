import requests

url = "http://127.0.0.1:8001/accounts/staff_assigned_leads/"

payload = {}
headers = {
  'Authorization': 'Bearer 1309bd750abee70042119ff2ef51356cdc07c23d'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
