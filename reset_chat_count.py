#!/usr/bin/python3

import os
import sqlite3

print(os.environ)

sqlite_file = 'ChatGPT.db'

# Connect to the SQLite database
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

sql = "UPDATE account SET chat_count = 0"

cursor.execute(sql)
print(cursor.rowcount, "record(s) affected")

# Commit the changes to the database and close the cursor and connection objects
connection.commit()
cursor.close()
connection.close()

# crontab command
# 0 3 * * * /usr/bin/python3 /home/azureuser/gpt/MyChatGPT/reset_chat_count.py
