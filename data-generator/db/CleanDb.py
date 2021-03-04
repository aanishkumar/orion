import sqlite3

connection = sqlite3.connect("../data.sqlite")
cursor = connection.cursor()
cursor.execute('DROP TABLE data')
connection.commit()
connection.close()
