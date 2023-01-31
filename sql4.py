import mysql.connector

# inserting data with tuples
connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
cursor = connection.cursor()
inserting_contato = "insert into contato (nome, telefone, celular) values (%s, %s, %s)"

data = ('Angela', '(41)999999999', '(41)33333333')

cursor.execute(inserting_contato, data)
connection.commit()
cursor.close()
