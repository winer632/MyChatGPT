# Import the modules
import flask
import mysql.connector
import recharge_callback
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename


# default value is 60
chat_count_setting = 60

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="gpt"
)
cursor = connection.cursor(dictionary=True)

sql = "SELECT chat_count_setting FROM settings"

cursor.execute(sql)
row = cursor.fetchone()
# Check if there are any rows in the result set
if row is not None:
    chat_count_setting = row["chat_count_setting"]
    print("[settings] chat_count_setting is ", chat_count_setting)

# Close the cursor and connection objects
cursor.close()
connection.close()


print("[after init] chat_count_setting is ", chat_count_setting)

# Create the flask app
app = flask.Flask(__name__)


# Define the validity endpoint
@app.route("/v1/auth", methods=["POST", "OPTIONS"])
def auth():
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
    # Create connection and cursor objects
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="gpt"
    )
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = %s AND expiration_date > NOW()"
    val = (access_key,)
    cursor.execute(sql, val)

    # Fetch the result
    row = cursor.fetchone()
    # Check if there are any rows in the result set
    if row is not None:
        print("[/v1/auth] access_key is ", access_key, " auth success")
        chat_count = row["chat_count"]
        if chat_count > chat_count_setting:
            print("[/v1/auth] No quota today. chat_count is ", chat_count, " chat_count_setting is ", chat_count_setting)
            response = flask.jsonify({"validation": "fail", "message": "No quota today"})
            # Set the CORS headers
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
            response.headers["Access-Control-Allow-Headers"] = "content-type"
            # Return the response object
            return response
        # update chat_count
        chat_count = row["chat_count"]+1
        sql = "UPDATE account SET chat_count = %s WHERE access_key = %s AND expiration_date > NOW()"
        val = (chat_count, access_key,)
        cursor.execute(sql, val)

        # Commit the changes to the database and close the cursor and connection objects
        connection.commit()
        cursor.close()
        connection.close()

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
        print("[/v1/auth] access_key is ", access_key, " auth fail")
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
    # Create connection and cursor objects
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="gpt"
    )
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = %s AND expiration_date > NOW()"
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
        print("[/v1/validity] access_key is ", access_key, " validation success")
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
        print("[/v1/validity] access_key is ", access_key, " validation fail")
        # Create a response object
        response = flask.jsonify({"validation": "fail", "message": "No valid subscription found"})
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response




# Define the validity endpoint
@app.route("/v1/chatcount", methods=["POST", "OPTIONS"])
def chatcount():
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
    # Create connection and cursor objects
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="gpt"
    )
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = %s AND expiration_date > NOW()"
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
        chat_count = row["chat_count"]
        available_number = chat_count_setting - chat_count
        print("[/v1/chatcount] access_key is ", access_key, " validation success. ", available_number, " more messages can be sent today" )
        # Create a response object
        response = flask.jsonify({"validation": "success", "message": str(available_number) + " more messages can be sent today"})
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response
    else:
        print("[/v1/chatcount] access_key is ", access_key, " validation fail")
        # Create a response object
        response = flask.jsonify({"validation": "fail", "message": "No valid subscription found"})
        # Set the CORS headers
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        # Return the response object
        return response