# Import modules
import mysql.connector
import secrets
import base64
from datetime import datetime, timedelta



# Define a function that takes the recharge amount as an argument
def recharge_callback_func(access_key, amount, product_id):
    # Create connection and cursor objects
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="gpt"
    )
    # create a cursor with dictionary argument
    cursor = connection.cursor(dictionary=True)

    # Select the unit_fee column from the table
    sql = "SELECT business_type, subscription_type, unit_fee, unit_validity_time FROM product where id = %s"
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
    print(type(add_validity_time))
    # convert it to an integer or float value
    add_validity_time = float(add_validity_time)
    print(type(add_validity_time))
    print("add_validity_time is ", add_validity_time)
        


    # Select the access_key column from the table
    sql = "SELECT access_key FROM account where business_type = %s and access_key = %s"
    val = (business_type, access_key)
    cursor.execute(sql, val)
    # fetch all rows
    row = cursor.fetchone()
    if row is not None:
        access_key = row["access_key"]
        print("access_key already exists ", access_key)        
        # Select the recharge_amount column from the table
        # sql = "SELECT expiration_date, recharge_amount FROM account where access_key = %s"
        # val = (access_key,)
        # cursor.execute(sql, val)
        # row = cursor.fetchone()
        # if row is not None:
        #     expiration_date = row["expiration_date"]
        #     recharge_amount = row["recharge_amount"]
        #     print("expiration_date is ", expiration_date)
        #     print("recharge_amount is ", recharge_amount)
        # else:
        #     print("No row found")
        #     expiration_date = datetime.now()
        #     recharge_amount = 0
        # accumulate_amount = amount+recharge_amount
        # print("history amount is ", recharge_amount)
        # print("current amount is ", amount)
        # print("accumulate_amount is ", accumulate_amount)
        # expiration_date = expiration_date + timedelta(seconds=add_validity_time)
        # print("new expiration_date is ", expiration_date)
        # # Update the record in the table with the new expiration date and recharge amount
        # sql = "UPDATE account set expiration_date = %s, recharge_amount=%s where access_key = %s"
        # val = (expiration_date, accumulate_amount, access_key,)
        # cursor.execute(sql, val)
    else:
        print("access_key does not exist")
        # Calculate the expiration date by adding the validity period to the current date and time
        expiration_date = datetime.now() + timedelta(seconds=add_validity_time)
        print("product_id is ", product_id)
        print("business_type is ", business_type)
        print("access_key is ", access_key)
        print("amount is ", amount)
        print("expiration_date is ", expiration_date)
        print("last_login_time is ", datetime.now())
        # Insert a new record into the table with the generated API key, recharge amount, expiration date, and last login time
        sql = "INSERT INTO account (product_id, business_type, access_key, recharge_amount, expiration_date, last_login_time) \
             VALUES (%s, %s, %s, %s, %s, %s)"
        val = (product_id, business_type, access_key, amount, expiration_date, datetime.now(),)
        cursor.execute(sql, val)

    # Commit the changes to the database and close the cursor and connection objects
    connection.commit()
    cursor.close()
    connection.close()
    

# Call the function with a sample recharge amount of 20 RMB
# recharge_callback_func('A9I67ijyubRhiJ6ZlXiR4zwBGmlI9TN_xbKxlnICfyA=',200,3)
