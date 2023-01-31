from mysql.connector import connection

# another form of connection
connection_mysql = connection.MySQLConnection(user="root", password="****", host="127.0.0.1", database="agenda")
connection_mysql.close()
