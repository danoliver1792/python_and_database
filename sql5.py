import mysql.connector

# entering data through a dictionary
connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
cursor = connection.cursor()

inserting_contato = ("insert into contato (nome, telefone, celular)"
                     " values (%(nome_contato)s, %(telefone)s, %(celular)s)")

contato = {
    "nome_contato": "Maria",
    "telefone": "(41)999999999",
    "celular": "(41)33333333"
}

cursor.execute(inserting_contato, contato)
connection.commit()
cursor.close()
connection.close()
