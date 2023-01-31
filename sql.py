import mysql.connector
from mysql.connector import errorcode

# handling error and connecting to the database "agenda"
try:
    connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error! Username or password is invalid")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error! Database does not exist")
    else:
        print("Error!")
else:
    connection.close()
