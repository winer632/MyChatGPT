# Import the modules
import requests

#change this to your api key and query if you are in your validity period
ACCESS_KEY = "ajbieaef23245678"
BASE_URL = "https://service.bizoe.tech/"

# Define a method for testing the validity endpoint
def test_validity():
    # Define a payload with a valid access key
    payload = {"access_key": "some_valid_id"}
    # Make a POST request to the validity endpoint
    response = requests.post(BASE_URL + "/v1/validity", json=payload, verify=False)
    print(response.json())
    print(response.json()["validation"])
    print(response.json()["message"])

# Define a method for testing the recharge endpoint
def test_recharge():
    # Define a payload with a valid payment intent ID, amount and business model ID
    payload = {"paymentIntentId": "some_valid_id", "amount": 1000, "business_model_id": 1}
    # Make a POST request to the recharge endpoint
    response = requests.post(BASE_URL + "/v1/recharge", json=payload, verify=False)
    print(response.json())

test_validity()
test_recharge()