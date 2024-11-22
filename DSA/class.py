import random


def generate_transaction_id():
        # while True:
    withdrawal_id = str(random.randint(1000000000, 9999999999))
            # if not MyUser.objects.filter(withdrawal_id=withdrawal_id).exists():
    return withdrawal_id

mywidid = generate_transaction_id()


# import requests
# import json

# url = "https://apideveloper.rblbank.com/test/sb/rbl/v1/payments/corp/payment/?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff"

# payload = json.dumps({
#   "Single_Payment_Corp_Req": {
#     "Header": {
#       "TranID": mywidid,
#       "Corp_ID": "SINGHTKLTD",
#       "Maker_ID": "M005",
#       "Checker_ID": "C003",
#       "Approver_ID": "A003"
#     },
#     "Body": {
#       "Amount": "200000.01",
#       "Debit_Acct_No": "409001591454",
#       "Debit_Acct_Name": "TEJU MAHTO",
#       "Debit_IFSC": "RBLB1122123",
#       "Debit_Mobile": "1234567890",
#       "Debit_TrnParticulars": "FARIDA",
#       "Debit_PartTrnRmks": "SURESH",
#       "Ben_IFSC": "DNSB0000021",
#       "Ben_Acct_No": "109566016481",
#       "Ben_Name": "SINGLE PAYMENT",
#       "Ben_Address": "MUMBAI",
#       "Ben_BankName": "ABC123123",
#       "Ben_BankCd": "176",
#       "Ben_BranchCd": "0123",
#       "Ben_Email": "mail@gmail.com",
#       "Ben_Mobile": "9895527234",
#       "Ben_TrnParticulars": "VIBEESH_@123",
#       "Ben_PartTrnRmks": "SINGLE PAYMENT",
#       "Issue_BranchCd": "0112",
#       "Mode_of_Pay": "RTGS",
#       "Remarks": "PAYEMNT QUEUE"
#     },
#     "Signature": {
#       "Signature": "Signature"
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

# # Path to your certificate and key files
# cert_path = 'D:\RBL SSL/cert_and_key.pem'
# # key_path = 'D:\RBL SSL/Password'

# response = requests.request("POST", url, headers=headers, data=payload, cert=(cert_path))

# print(response.text, 'aaaaaaaaaaaaaaaaaaaaaaaaaa')





# ------------------------------------   ---------------------- ----------------




#-----------------------------------------------

import http.client
import json
import ssl
import os

url = "apideveloper.rblbank.com"

payload = json.dumps({
  "Single_Payment_Corp_Req": {
    "Header": {
      "TranID": mywidid,
      "Corp_ID": "SINGHTKLTD",
      "Maker_ID": "M005",
      "Checker_ID": "C003",
      "Approver_ID": "A003"
    },
    # "Body": {
    #   "Amount": "100.01",
    #   "Debit_Acct_No": "409001591454",
    #   "Debit_Acct_Name": "TEJU MAHTO",
    #   "Debit_IFSC": "RBLB1122123",
    #   "Debit_Mobile": "1234567890",
    #   "Debit_TrnParticulars": "FARIDA",
    #   "Debit_PartTrnRmks": "SURESH",
    #   "Ben_IFSC": "DNSB0000021",
    #   "Ben_Acct_No": "109566016481",
    #   "Ben_Name": "SINGLE PAYMENT",
    #   "Ben_Address": "MUMBAI",
    #   "Ben_BankName": "ABC123123",
    #   "Ben_BankCd": "176",
    #   "Ben_BranchCd": "0123",
    #   "Ben_Email": "mail@gmail.com",
    #   "Ben_Mobile": "9895527234",
    #   "Ben_TrnParticulars": "VIBEESH_@123",
    #   "Ben_PartTrnRmks": "SINGLE PAYMENT",
    #   "Issue_BranchCd": "0112",
    #   "Mode_of_Pay": "NEFT",
    #   "Remarks": "PAYEMNT QUEUE"
    # },

    # "Body": {
		# 	"Amount": "2",
		# 	"Debit_Acct_No": "1000112010000333",
		# 	"Debit_Acct_Name": "TEJU MAHTO",
		# 	"Debit_IFSC": "RBLB1122123",
		# 	"Debit_Mobile": "1234567890",
		# 	"Debit_TrnParticulars": "FARIDA",
		# 	"Debit_PartTrnRmks": "SURESH",
		# 	"Ben_IFSC": "DNSB0000021",
		# 	"Ben_Acct_No": "1256905",
		# 	"Ben_Name": "SINGLE PAYMENT",
		# 	"Ben_Address": "MUMBAI",
		# 	"Ben_BankName": "ABC123123",
		# 	"Ben_BankCd": "176",
		# 	"Ben_BranchCd": "0123",
		# 	"Ben_Email": "mail@gmail.com",
		# 	"Ben_Mobile": "9895527234",
		# 	"Ben_TrnParticulars": "VIBEESH_@123",
		# 	"Ben_PartTrnRmks": "SINGLE PAYMENT",
		# 	"Issue_BranchCd": "0112",
		# 	"Mode_of_Pay": "IMPS",
		# 	"Remarks": "PAYEMNT QUEUE"		
		# },
        
    "Body": {
			"Amount": "2",
			"Debit_Acct_No": "1000112010000333",
			"Debit_Acct_Name": "TEJU MAHTO",
			"Debit_IFSC": "RBLB1122123",
			"Debit_Mobile": "1234567890",
			"Debit_TrnParticulars": "FARIDA",
			"Debit_PartTrnRmks": "SURESH",
			"Ben_IFSC": "DNSB0000021",
			"Ben_Acct_No": "1256905",
			"Ben_Name": "SINGLE PAYMENT",
			"Ben_Address": "MUMBAI",
			"Ben_BankName": "ABC123123",
			"Ben_BankCd": "176",
			"Ben_BranchCd": "0123",
			"Ben_Email": "mail@gmail.com",
			"Ben_Mobile": "9895527234",
			"Ben_TrnParticulars": "VIBEESH_@123",
			"Ben_PartTrnRmks": "SINGLE PAYMENT",
			"Issue_BranchCd": "0112",
			"Mode_of_Pay": "RTGS",
			"Remarks": "PAYEMNT QUEUE"		
		},



    "Signature": {
      "Signature": "Signature"
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
connection.request("POST", "/test/sb/rbl/v1/payments/corp/payment/?client_id=fd4ece93f78eac9125f482172c05b6b6&client_secret=d974f70d3015eda50af73b75ee5481ff", body=payload, headers=headers)
response = connection.getresponse()
print(response.status, response.reason, response.read().decode(), 'SSSSSSSSSSSSSSSSSSSSSSSSSSSS')

# Read the response data
# response_data = response.read().decode()

# Close the connection
connection.close()


# Parse the JSON response
# response_json = json.loads(response_data)

# Extract the status
# status = response_json['Single_Payment_Corp_Req']['Header']['Status']

# Print the status
# print(status, 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')

# ---------------------------------------------------------------

# Parse the JSON string
# response = json.loads(payload)
# print(response['Single_Payment_Corp_Resp']['Header']['Status'], 'AAAAAAAAAAAAAAAAAAAAAAA')

# except Exception as e:
#     print(str(e), 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')



