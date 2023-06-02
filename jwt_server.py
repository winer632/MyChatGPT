# Import the modules
import flask
import jwt
import mysql.connector
import recharge_callback
from datetime import datetime, timedelta

# Create the flask app
app = flask.Flask(__name__)

# Define the secret key for JWT
SECRET_KEY = "vs63TVu7HD_8ofiqBKZZ-D4sDqTo1003x05tS7o5j6c"


# Define the validity endpoint
@app.route("/v1/validity", methods=["POST"])
def validity():
    # Get the request data
    data = flask.request.get_json()

    # Get the authorization header
    auth_header = flask.request.headers.get("Authorization")

    # Check if the header is valid
    if auth_header and auth_header.startswith("Bearer "):
        # Extract the token from the header
        token = auth_header.split(" ")[1]

        # Decode the token and verify the payload
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            ACCESS_KEY = payload["sub"]
            business_type = payload["business_type"]
            print("ACCESS_KEY is ", ACCESS_KEY)
            print("business_type is ", business_type)
            # Check the type of the request data
            if data["type"] == "trial" or data["type"] == "subscription":
                # Create connection and cursor objects
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456",
                    database="gpt"
                )
                cursor = connection.cursor(dictionary=True)

                # Execute a SQL query
                sql = "SELECT expiration_date FROM account WHERE business_type = %s AND UNIX_TIMESTAMP(expiration_date) > UNIX_TIMESTAMP() AND access_key = %s"
                val = (business_type, ACCESS_KEY,)
                cursor.execute(sql, val)
                

                # Fetch the result
                row = cursor.fetchone()
                # Commit the changes to the database and close the cursor and connection objects
                connection.commit()
                cursor.close()
                connection.close()

                # Check if there are any rows in the result set
                if row is not None:
                    expiration_date = row["expiration_date"]
                    # Return a success response
                    return flask.jsonify({"validation":"success", "expiration_date":expiration_date})
                else:
                    # Return fail
                    return flask.jsonify({"validation": "fail"})
            else:
                # Return a fail response
                return flask.jsonify({"validation": "fail"})
            
        except jwt.InvalidTokenError:
            # Return a fail response
            return flask.jsonify({"validation": "fail"})
    else:
        # Return a fail response
        return flask.jsonify({"validation": "fail"})
    
# Define the recharge endpoint
@app.route("/v1/recharge", methods=["POST"])
def recharge():
    # Get the request data
    # https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-line_items
    data = flask.request.get_json()
    access_key = data["customer"] # customer ID of an existing Customer, if one exists.
    amount = data["amount"] # line_items.quantity When set, provides configuration for this item’s quantity to be adjusted by the customer during Checkout.
    business_model_id = data["business_model_id"] # line_items.price_data Data used to generate a new Price object inline. One of price or price_data is required.
    client_reference_id = data["client_reference_id"] # client_reference_id A unique string to reference the Checkout Session. 
    email = data["email"]
    phone = data["phone"]
    currency = data["currency"] # currency The currency of the Checkout Session. Required if using line_items.price_data. Must match the currency associated with your Stripe account.
    recharge_callback(access_key, amount, business_model_id, client_reference_id, email, phone)

# use gunicorn to run in production environment  
# gunicorn -w 5 -b 127.0.0.1:2023 jwt_server:app
# Run the app
#if __name__ == "__main__":
#    app.run(port=8080)
