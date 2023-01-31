import mysql.connector

# creating the connection and the cursor to move through the records
connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
cursor = connection.cursor()

# inserting the data
inserting_contato = ("insert into contato (nome, telefone, celular) "
                     "values ('Danrlei', '(41)999999999', '(41)33333333')")

# running the command
cursor.execute(inserting_contato)
connection.commit()
cursor.close()
connection.close()
