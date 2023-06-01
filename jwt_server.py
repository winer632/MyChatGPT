# Import the modules
import flask
import jwt
import mysql.connector
from datetime import datetime, timedelta

# Create the flask app
app = flask.Flask(__name__)

# Define the secret key for JWT
SECRET_KEY = "vs63TVu7HD_8ofiqBKZZ-D4sDqTo1003x05tS7o5j6c"


# Define the validity endpoint
@app.route("/v1/chat/validity", methods=["POST"])
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
            print("ACCESS_KEY is ", ACCESS_KEY)
            # Check the type of the request data
            if data["type"] == "trial" or data["type"] == "subscription":
                # Create connection and cursor objects
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456",
                    database="gpt"
                )
                cursor = connection.cursor()

                # Execute a SQL query
                sql = "SELECT expiration_date FROM account WHERE UNIX_TIMESTAMP(expiration_date) > UNIX_TIMESTAMP() AND access_key = %s"
                val = (ACCESS_KEY,)
                cursor.execute(sql, val)
                

                # Fetch all the rows from the result set
                rows = cursor.fetchall()
                # Commit the changes to the database and close the cursor and connection objects
                connection.commit()
                cursor.close()
                connection.close()

                # Check if there are any rows in the result set
                if rows:
                    # Return a success response
                    return flask.jsonify({"validation": "success"})
                else:
                    # Return false
                    return flask.jsonify({"validation": "false"})
            else:
                # Return a fail response
                return flask.jsonify({"validation": "fail"})
            
        except jwt.InvalidTokenError:
            # Return a fail response
            return flask.jsonify({"validation": "fail"})
    else:
        # Return a fail response
        return flask.jsonify({"validation": "fail"})

# Run the app
if __name__ == "__main__":
    app.run(port=8080)
