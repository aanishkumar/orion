import csv
import sqlite3

connection = sqlite3.connect("../data.sqlite")
cursor = connection.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS data ("PIDNo" text, "Full Name text", "Name" text, "First Name" text,
     "Last Name" text, "Appointed (ERP) Office Name" text, "Appointed (ERP) Office Town" text,
      "Appointed (ERP) Office Postcode" text, "Appointed (ERP) GOR" text, "OfficeLat" text, "OfficeLong" text,
       "Steps Code" text, "Contract Type" text, "Employee Group" text, "Perm/Temp" text, "FTA End Date" text,
        "Grade" text, "HMRC Grade" text, "SiP Grade" text, "SIP Grade (FTA)" text)''')

data_file = open("data.csv")
rows = csv.reader(data_file)
next(rows)
cursor.executemany("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

connection.commit()
connection.close()
