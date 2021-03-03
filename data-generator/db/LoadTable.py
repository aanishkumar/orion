import csv
import sqlite3

connection = sqlite3.connect("../data.sqlite")
cursor = connection.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS data (Email Id text,Prefix text,Name text,Birth Date text,Phone Number text,
    Additional Email Id text,Address text,Zip Code text,City text,State text,Country text,Year text,Time text,
    Link text ,Text text)''')

data_file = open("data.csv")
rows = csv.reader(data_file)
next(rows)
cursor.executemany("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

connection.commit()
connection.close()
