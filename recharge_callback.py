# Import modules
import sqlite3
import secrets
import base64
from datetime import datetime, timedelta

sqlite_file = 'ChatGPT.db'

# Define a function that takes the recharge amount as an argument
def recharge_callback_func(access_key, amount, product_id):
    # Create connection object
    connection = sqlite3.connect(sqlite_file)
    connection.row_factory = sqlite3.Row  # This will allow us to access rows as dictionaries
    cursor = connection.cursor()

    # Select the unit_fee column from the table
    sql = "SELECT business_type, subscription_type, unit_fee, unit_validity_time FROM product WHERE product_id = ?"
    val = (product_id,)
    cursor.execute(sql, val)

    row = cursor.fetchone()
    if row is not None:
        # get column values by name
        business_type = row["business_type"]
        subscription_type = row["subscription_type"]
        unit_fee = row["unit_fee"]
        unit_validity_time = row["unit_validity_time"]
        
        print("business_type is ", business_type)
        print("subscription_type is ", subscription_type)
        print("unit_fee is ", unit_fee)
        print("unit_validity_time is ", unit_validity_time)
    else:
        print("No row found")
        return
    add_validity_time = (amount/unit_fee)*unit_validity_time
    add_validity_time = float(add_validity_time)
    print("add_validity_time is ", add_validity_time)

    # Select the access_key column from the table
    sql = "SELECT access_key FROM account WHERE access_key = ?"
    val = (access_key,)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    if row is not None:
        access_key = row["access_key"]
        print("access_key already exists ", access_key)
    else:
        print("access_key does not exist")
        # Calculate the expiration date by adding the validity period to the current date and time
        expiration_date = datetime.now() + timedelta(seconds=add_validity_time)
        # Insert a new record into the table with the generated API key, recharge amount, expiration date, and last login time
        sql = "INSERT INTO account (product_id, business_type, access_key, recharge_amount, expiration_date, last_login_time) \
             VALUES (?, ?, ?, ?, ?, ?)"
        val = (product_id, business_type, access_key, amount, expiration_date, datetime.now())
        cursor.execute(sql, val)

    # Commit the changes to the database and close the cursor and connection objects
    connection.commit()
    cursor.close()
    connection.close()

