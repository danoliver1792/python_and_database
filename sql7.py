import mysql.connector

# deleting record
connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
cursor = connection.cursor()

delete_contato = "delete from contato where nome = 'Vitoria'"

cursor.execute(delete_contato)
connection.commit()
cursor.close()
connection.close()
