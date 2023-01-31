import mysql.connector

# updating data
connection = mysql.connector.connect(user="root", password="****", host="127.0.0.1", database="agenda")
cursor = connection.cursor()

update_contato = "update contato set nome = %s, telefone = %s, celular = %s where nome = 'Maria'"
contato = ('Vitoria', "(41)992222222", "(41)32999999")

cursor.execute(update_contato, contato)
connection.commit()
cursor.close()
connection.close()
