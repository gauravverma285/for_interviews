# import requests

# # Function to get geolocation data
# def get_geolocation(ip_address):
#     # Use the ipinfo.io API to get location data
#     response = requests.get(f"https://ipinfo.io/{ip_address}/json")

#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "IP": data.get("ip"),
#             "City": data.get("city"),
#             "Region": data.get("region"),
#             "Country": data.get("country"),
#             "Location": data.get("loc"),  # Latitude and Longitude
#             "ISP": data.get("org"),       # Internet Service Provider
#             "Timezone": data.get("timezone")
#         }
#     else:
#         return {"error": "Unable to fetch data"}

# # Example usage
# ip_address = "192.168.0.112"  # Example IP address (Google Public DNS)
# location_data = get_geolocation(ip_address)

# print(location_data)



import requests

# Function to get the public IP address
def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip_data = response.json()
    return ip_data["ip"]

# Function to get geolocation data
def get_geolocation(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    if response.status_code == 200:
        data = response.json()
        return {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),
            "ISP": data.get("org"),
            "Timezone": data.get("timezone")
        }
    else:
        return {"error": "Unable to fetch data"}

# Example usage
public_ip = get_public_ip()
location_data = get_geolocation("152.58.70.34")

print(location_data)

