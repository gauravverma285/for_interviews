import http.client
import json
import ssl
import os

url = "apideveloper.rblbank.com"

payload = json.dumps({
  "get_Single_Payment_Status_Corp_Req": {
    "Header": {
      "TranID": "6611574187",
      "Corp_ID": "SINGHTKLTD",
      "Maker_ID": "",
      "Checker_ID": "",
      "Approver_ID": ""
    },
    "Body": {
      "UTRNo": "RATNH24197291947"
    },
    "Signature": {
      "Signature": "Signature"
    }
  }
})
headers = {
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
connection.request("POST", "/test/sb/rbl/v1/payments/corp/payment/query/?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff", body=payload, headers=headers)
response = connection.getresponse()
print(response.status, response.reason, response.read().decode(), 'SSSSSSSSSSSSSSSSSSSSSSSSSSSS')

# Read the response data
# response_data = response.read().decode()

# Close the connection
connection.close()


# Parse the JSON response
# response_json = json.loads(response_data)

# # Extract the status
# status = response_json['Single_Payment_Corp_Resp']['Header']['Status']

# # Print the status
# print(status, 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')









# import http.client
# import json
# import ssl

# url = "apideveloper.rblbank.com"

# payload = json.dumps({
#   "get_Single_Payment_Status_Corp_Req": {
#     "Header": {
#       "TranID": "6611574187",
#       "Corp_ID": "SINGHTKLTD",
#       "Maker_ID": "M005",
#       "Checker_ID": "C003",
#       "Approver_ID": "A003"
#     },
#     "Body": {
#       "UTRNo": "RATNH24197291947"
#     },
#     "Signature": {
#       "Signature": "Signature"
#     }
#   }
# })

# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic U0lOR0hUS0xURDpXZWxjb21lQDEyMw==',
#   'TranID': '1Abc22249Q13',
#   'Corp_ID': 'ZSA01',
#   'Maker_ID': 'M005',
#   'Checker_ID': 'C003',
#   'Approver_ID': 'A003'
# }

# # Path to your certificate and key files
# cert_path = r'D:\RBL SSL\cert_and_key.pem'

# # Create an SSL context and load the certificate and key
# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# context.load_cert_chain(certfile=cert_path)

# try:
#     connection = http.client.HTTPSConnection(url, context=context)
#     endpoint = "/test/sb/rbl/v1/payments/corp/payment/query/?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff"
#     connection.request("POST", endpoint, body=payload, headers=headers)
#     response = connection.getresponse()

#     status_code = response.status
#     reason = response.reason
#     response_data = response.read().decode()

#     print(status_code, reason)
#     print(response_data)

#     # Parse the JSON response if needed
#     # response_json = json.loads(response_data)
#     # status = response_json['Single_Payment_Corp_Resp']['Header']['Status']
#     # print(status)

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     connection.close()







# ----------------------------------------

# import http.client
# import json
# import ssl


# # Path to your certificate and key files
# cert_path = r'D:\RBL SSL\cert_and_key.pem'

# # Create an SSL context and load the certificate and key
# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# context.load_cert_chain(certfile=cert_path)
# conn = http.client.HTTPSConnection("apideveloper.rblbank.com", context=context)

# payload = json.dumps({
#   "get_Single_Payment_Status_Corp_Req": {
#     "Header": {
#       "TranID": "6611574187",
#       "Corp_ID": "SINGHTKLTD",
#       "Maker_ID": "",
#       "Checker_ID": "",
#       "Approver_ID": ""
#     },
#     "Body": {
#       "UTRNo": "RATNH24197291947"
#     },
#     "Signature": {
#       "Signature": "Signature"
#     }
#   }
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic U0lOR0hUS0xURDpXZWxjb21lQDEyMw=='
# }
# conn.request("POST", "/test/sb/rbl/v1/payments/corp/payment/query?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))
