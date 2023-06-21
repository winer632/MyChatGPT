import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="gpt"
)
cursor = connection.cursor(dictionary=True)

sql = "UPDATE account SET chat_count = 0"

cursor.execute(sql)
print(cursor.rowcount, "record(s) affected")

# Commit the changes to the database and close the cursor and connection objects
connection.commit()
cursor.close()
connection.close()


# crontab command
# 0 3 * * * /usr/bin/python3 /home/azureuser/gpt/MyChatGPT/reset_chat_count.py
