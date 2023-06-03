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

@app.route('/v1/webhook', methods=['POST'])
def webhook():
  # Check if webhook signing is configured.
  if endpoint_secret:
    # Retrieve the event by verifying the signature using the raw body and secret.
    event = None
    signature = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            request.data, 
			signature, 
			endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      payment_intent = event['data']['object'] # contains a stripe.PaymentIntent
      print("payment_intent.id is ", payment_intent.id)
      print("payment_intent.amount is ", payment_intent.amount)
      print("payment_intent.currency is ", payment_intent.currency)
      print("payment_intent.customer is ", payment_intent.customer)
      print("payment_intent.payment_method is ", payment_intent.payment_method)
      print("payment_intent.payment_method_types is ", payment_intent.payment_method_types)
      


      access_key = payment_intent.metadata.access_key
      amount = payment_intent.amount
      business_model_id = payment_intent.metadata.business_model_id
      client_reference_id = payment_intent.metadata.client_reference_id
      email = payment_intent.metadata.customer_email
      phone = payment_intent.metadata.customer_phone
      payment_intent.currency
      

    if event['type'] == 'checkout.session.completed':
      print("🔔  Payment received!")
      session = event['data']['object']
      print("session is ", session)
      # Get the custom fields array from the event data
      custom_fields = event['data']["object"]["custom_fields"]
      # Loop through the custom fields and find the one with key "access_key"
      for field in custom_fields:
        if field["key"] == "access_key":
          # Get the access_key value from the field
          access_key = field["text"]["value"]
          # Do something with the access_key value
          print(f"Access key: {access_key}")
          recharge_callback(access_key, amount, business_model_id, client_reference_id, email, phone)
    elif event['type'] == 'checkout.session.async_payment_failed':
      print("🔔  Async Payment failed!")
    elif event['type'] == 'checkout.session.async_payment_succeeded':
      print("🔔  Async Payment succeeded!")
    elif event['type'] == 'checkout.session.expired':
      print("🔔  Checkout Session expired!")
    # ... handle other event types
    else:
      print('Unhandled event type {}'.format(event['type']))
      return 'Unhandled event type {}'.format(event['type']), 422
    return jsonify(success=True)


# Use gunicorn to run in production environment  
# Run gunicorn with HTTPS on port 443
# gunicorn -w 5 -b 0.0.0.0:443 --certfile openssl/server.crt --keyfile openssl/server.key webhook:app
# Note that port 443 is a privileged port, so you may need to run the command with sudo or as root user.