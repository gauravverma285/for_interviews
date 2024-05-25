import urllib.request
import json
import time
import random

def generate_otp():
    # Replace this with your actual OTP generation logic
    return random.randint(10000, 99999)

def send_otp(phone, otp):
	# phone = "9982908095"
	# otp = "123456"
	url = "http://nimbusit.info/api/pushsmsjson.php"
	body = {
		"Authorization": {
			"User": "102309",
			"Key": "010FG3iI10ylPJ4Yefgw"
		},
		"Data": {
			"Sender": "INNOAS",
			"Message": "<  # > Dear Customer Come, Come, " + "Come bhujo to jaane " + str(otp) + " is your One Time Password to verify your mobile number on Woodland interior & exterior "  + " website. \n\n\n INNOVANA",
			"Flash": 0,
			"RefrenceId": "12345",
			"EntityId": "1701161823476309576",
						"TemplateId": "1707161891161722443",
						"Mobile": [
							phone
						]
		}
	}
	req = urllib.request.Request(url)
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	data = json.dumps(body).encode('utf-8')
	response = urllib.request.urlopen(req, data)
	return response

for i in range(10):
    otp = generate_otp()
    # print(send_otp(9982908095, otp), 'AAAAAAAAAAAAAA')
    print(send_otp(7230833160, otp), 'AA')
    time.sleep(3)