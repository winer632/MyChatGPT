# Import the modules
import flask
import mysql.connector
import recharge_callback
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

# Create the flask app
app = flask.Flask(__name__)

# Define the secret key for JWT
SECRET_KEY = "vs63TVu7HD_8ofiqBKZZ-D4sDqTo1003x05tS7o5j6c"


# Define the validity endpoint
@app.route("/v1/validity", methods=["POST", "OPTIONS"])
def validity():
    # Check if the request is an OPTIONS request
    if request.method == "OPTIONS":
        # Create an empty response object
        response = flask.Response("")
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response

    # Get the payload as a JSON object
    payload = request.get_json()
    access_key = payload["access_key"]
    print("access_key is ", access_key)
    # Create connection and cursor objects
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="gpt"
    )
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT expiration_date FROM account USE INDEX (access_key_expiration_date) WHERE expiration_date > NOW() AND access_key = %s"
    val = (access_key,)
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
        # Create a response object
        response = flask.jsonify({"validation":"success", "message":"valid until "+expiration_date.strftime("%Y-%m-%d %H:%M:%S")})
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response
    else:
        # Create a response object
        response = flask.jsonify({"validation": "fail", "message": "No valid subscription found"})
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response

    
@app.route('/v1/recharge', methods=['POST', 'OPTIONS'])
def recharge():
    # Check if the request is an OPTIONS request
    if request.method == "OPTIONS":
        # Create an empty response object
        response = flask.Response("")
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response

    # Get the payload as a JSON object
    payload = request.get_json()
    access_key = payload['paymentIntentId']
    amount = payload['amount']
    product_id = payload['product_id']
    print("access_key is ", access_key)
    print("amount is ", amount)
    print("product_id is ", product_id)
    recharge_callback.recharge_callback_func(access_key, amount, product_id)

    # Create a response object
    response = jsonify(success=True)
    # Set the CORS headers
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "content-type"
    # Return the response object
    return response

