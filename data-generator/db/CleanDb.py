import sqlite3

con = sqlite3.connect("../hmdata.sqlite")
cur = con.cursor()
cur.execute('DROP TABLE data')
con.commit()
con.close()
