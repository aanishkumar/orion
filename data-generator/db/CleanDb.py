import sqlite3

con = sqlite3.connect("../data.sqlite")
cur = con.cursor()
cur.execute('DROP TABLE data')
con.commit()
con.close()
