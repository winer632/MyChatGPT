# Import the modules
import flask
import sqlite3
import recharge_callback
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename


# default value is 60
chat_count_setting = 60

sqlite_file = 'ChatGPT.db'

connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

sql = "SELECT chat_count_setting FROM settings"

cursor.execute(sql)
row = cursor.fetchone()
# Check if there are any rows in the result set
if row is not None:
    # Convert the row to a dictionary
    row = {description[0]: value for description, value in zip(cursor.description, row)}
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
    print(payload)
    access_key = payload["access_key"]
    model = payload["model"]
    # Create connection and cursor objects
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = ? AND expiration_date > datetime('now')"
    val = (access_key,)
    cursor.execute(sql, val)

    # Fetch the result
    row = cursor.fetchone()
    # Check if there are any rows in the result set
    if row is not None:
        print("[/v1/auth] access_key is ", access_key, " auth success")
        # Convert the row to a dictionary
        row = {description[0]: value for description, value in zip(cursor.description, row)}
        chat_count = row["chat_count"]
        if chat_count >= chat_count_setting:
            print("[/v1/auth] No quota today. chat_count is ", chat_count, " chat_count_setting is ", chat_count_setting)
            response = flask.jsonify({"validation": "insufficient quota", "message": "No quota today. You have sent "+str(chat_count)+
                                      " messages today. Your quota is "+str(chat_count_setting)+" messages per day"})
            # Set the CORS headers
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, OPTIONS, DELETE"
            response.headers["Access-Control-Allow-Headers"] = "content-type"
            # Return the response object
            return response
        # update chat_count
        if  (model.startswith("gpt-4o")):
            print("usig gpt-4o, chat_count before is ", chat_count)
            chat_count = row["chat_count"]+6
            print("usig gpt-4o, chat_count now is ", chat_count)
        elif (model.startswith("gpt-4-")):
            print("usig gpt-4, chat_count before is ", chat_count)
            chat_count = row["chat_count"]+12
            print("usig gpt-4, chat_count now is ", chat_count)
        else:
            print("usig gpt-3.5, chat_count before is ", chat_count)
            chat_count = row["chat_count"]+1
            print("usig gpt-3.5, chat_count now is ", chat_count)
        sql = "UPDATE account SET chat_count = ? WHERE access_key = ? AND expiration_date > datetime('now')"
        val = (chat_count, access_key,)
        cursor.execute(sql, val)

        # Commit the changes to the database and close the cursor and connection objects
        connection.commit()
        cursor.close()
        connection.close()

        expiration_date = row["expiration_date"]
        # Create a response object
        response = flask.jsonify({"validation":"success", "message":"valid until "+expiration_date})
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
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = ? AND expiration_date > datetime('now')"
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
        # Convert the row to a dictionary
        row = {description[0]: value for description, value in zip(cursor.description, row)}
        expiration_date = row["expiration_date"]
        # Create a response object
        response = flask.jsonify({"validation":"success", "message":"valid until " + expiration_date})
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
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    sql = "SELECT expiration_date, chat_count FROM account WHERE access_key = ? AND expiration_date > datetime('now')"
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
        # Convert the row to a dictionary
        row = {description[0]: value for description, value in zip(cursor.description, row)}
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
    
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=6666)