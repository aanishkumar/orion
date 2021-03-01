import csv
import sqlite3

conn = sqlite3.connect("../data.sqlite")
cur = conn.cursor()
cur.execute(
    '''CREATE TABLE IF NOT EXISTS data (Email Id text,Prefix text,Name text,Birth Date text,Phone Number text,
    Additional Email Id text,Address text,Zip Code text,City text,State text,Country text,Year text,Time text,
    Link text ,Text text)''')

a_file = open("data.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

conn.commit()
conn.close()
