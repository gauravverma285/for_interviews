# import requests
# import json

# url = "https://gateway.rblbank.com/prod/sb/rbl/v1/blob/statement/?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff"

# payload = json.dumps({
#   "FetchAccStmtReq": {
#     "Header": {
#       "TranID": "123",
#       "Corp_ID": "VISTAARFIN",
#       "account_no": "409000770146",
#       "from_date": "02-03-2020",
#       "to_date": "27-03-2020",
#       "bucket": "1"
#     }
#   }
# })
# headers = {
#   'TranID': '1Abc22249Q13',
#   'Corp_ID': 'ZSA01',
#   'Maker_ID': 'M005',
#   'Checker_ID': 'C003',
#   'Approver_ID': 'A003',
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic U0lOR0hUS0xURDpXZWxjb21lQDEyMw=='
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)




import http.client
import json
import ssl
import os

url = "apideveloper.rblbank.com"

payload = json.dumps({
  "FetchAccStmtReq": {
    "Header": {
      "TranID": "123",
      "Corp_ID": "VISTAARFIN",
      "account_no": "409000770146",
      "from_date": "02-03-2020",
      "to_date": "27-03-2020",
      "bucket": "1"
    }
  }
})

headers = {
  'TranID': '1Abc22249Q13',
  'Corp_ID': 'ZSA01',
  'Maker_ID': 'M005',
  'Checker_ID': 'C003',
  'Approver_ID': 'A003',
  'Content-Type': 'application/json',
  'Authorization': 'Basic U0lOR0hUS0xURDpXZWxjb21lQDEyMw=='
}

# Path to your certificate and key files
cert_path = r'D:\RBL SSL\cert_and_key.pem'

# Create an SSL context and load the certificate and key
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile=cert_path)

# try:
connection = http.client.HTTPSConnection(url, context=context)
connection.request("GET", "/prod/sb/rbl/v1/blob/statement?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff", body=payload, headers=headers)
response = connection.getresponse()
print(response.status, response.reason, response.read().decode(), 'SSSSSSSSSSSSSSSSSSSSSSSSSSSS')

# Read the response data
# response_data = response.read().decode()

# Close the connection
connection.close()
