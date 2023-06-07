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
@app.route("/v1/validity", methods=["POST"])
def validity():
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

    # Execute a SQL query
    sql = "SELECT expiration_date FROM account WHERE UNIX_TIMESTAMP(expiration_date) > UNIX_TIMESTAMP() AND access_key = %s"
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
        # Return a success response
        return flask.jsonify({"validation":"success", "message":"valid until "+expiration_date.strftime("%Y-%m-%d %H:%M:%S")})
    else:
        # Return fail
        return flask.jsonify({"validation": "fail", "message": "No valid subscription found"})

    
@app.route('/v1/recharge', methods=['POST'])
def recharge():
    # Get the payload as a JSON object
    payload = request.get_json()
    access_key = payload['paymentIntentId']
    amount = payload['amount']
    product_id = payload['product_id']
    print("access_key is ", access_key)
    print("amount is ", amount)
    print("product_id is ", product_id)
    recharge_callback.recharge_callback_func(access_key, amount, product_id)


    return jsonify(success=True)



@app.route("/upload", methods=["POST"])
def upload_file():
  # get the file from the request
  file = request.files["file"]

  # check if the file is valid
  if file:
    # get the secure file name
    filename = secure_filename(file.filename)

    # save the file to the /.well-known/pki-validation/ folder
    file.save("./.well-known/pki-validation/" + filename)

    # redirect to some success page
    return redirect("/success")
  else:
    # return some error message
    return "No file selected"


# use gunicorn to run in production environment  
# gunicorn -w 5 -b 127.0.0.1:2023 jwt_server:app
# Run the app
#if __name__ == "__main__":
#    app.run(port=8080)
