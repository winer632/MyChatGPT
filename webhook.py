# app.py
#
# Use this sample code to handle webhook events in your integration.
#
# 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe
import recharge_callback
from dotenv import load_dotenv, find_dotenv

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

app = Flask(__name__)

@app.route('/v1/recharge', methods=['POST'])
def webhook():
    # Get the payload as a JSON object
    payload = request.get_json()
    access_key = payload['paymentIntentId']
    amount = payload['amount']
    business_model_id = payload['business_model_id']
    recharge_callback(access_key, amount, business_model_id)


    return jsonify(success=True)


# Use gunicorn to run in production environment  
# Run gunicorn with HTTPS on port 443
# gunicorn -w 5 -b 0.0.0.0:443 --certfile openssl/server.crt --keyfile openssl/server.key webhook:app
# Note that port 443 is a privileged port, so you may need to run the command with sudo or as root user.