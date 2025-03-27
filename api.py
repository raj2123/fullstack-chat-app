import requests
from requests.auth import HTTPBasicAuth

# Cloudinary credentials
CLOUD_NAME = "dgh6gvkds"
API_KEY = "263941314414239"
API_SECRET = "r8mZkmsVveTJ_ZMjKNVKkQm9iSk"

# Cloudinary API URL
url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/resources/image"

# Make the request
response = requests.get(url, auth=HTTPBasicAuth(API_KEY, API_SECRET))

# Check the response
if response.status_code == 200:
    print("✅ Cloudinary credentials are valid!")
    print("Response:", response.json())
elif response.status_code == 401:
    print("❌ Invalid Cloudinary credentials!")
else:
    print(f"⚠️ Unexpected status code: {response.status_code}")
    print("Response:", response.text)
