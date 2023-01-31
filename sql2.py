import mysql.connector

# connecting with a dictionary
config = {
    "user": "root",
    "password": "****",
    "host": "127.0.0.1",
    "database": "agenda"
}

connection = mysql.connector.connect(**config)
connection.close()
