# Import the modules
import requests
import jwt

# Define the URL and the data
url = "http://20.24.36.19:2023/v1/validity"
data = {"type": "trial"} # or {"type": "subscription"}

#change this to your api key and query if you are in your validity period
ACCESS_KEY = "jfwkgMx7xK8kZ0U4u2NZvd_-5iVdmRxtU5ux1DAKQ3o="

# Define the secret key and the payload for JWT
secret_key = "vs63TVu7HD_8ofiqBKZZ-D4sDqTo1003x05tS7o5j6c"
# business_type include basic_chat, internet_chat, pdf and so on
# subscription_type include trial，per_month，per_year
# access_key should be unique in the scope of business_type
payload = {
    "sub": ACCESS_KEY,
    "business_type": "basic_chat",
    "iat": 1516239022
}

# Encode the payload and generate the token
token = jwt.encode(payload, secret_key, algorithm="HS256")

# Define the headers with the token
headers = {
    "Authorization": f"Bearer {token}"
}

# Send the POST request and get the response
response = requests.post(url, json=data, headers=headers)

# Print the response status code and data
print(response.status_code)
print(response.json())
