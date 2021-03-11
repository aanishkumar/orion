import csv
import sqlite3

connection = sqlite3.connect("../data.sqlite")
cursor = connection.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS data ("PIDNo" text, "Full Name" text, "Name" text, "First Name" text,
     "Last Name" text, "Appointed (ERP) Office Name" text, "Appointed (ERP) Office Town" text,
      "Appointed (ERP) Office Postcode" text, "Appointed (ERP) GOR" text, "OfficeLat" text, "OfficeLong" text,
       "Steps Code" text, "Contract Type" text, "Employee Group" text, "Perm/Temp" text, "FTA End Date" text,
        "Grade" text, "HMRC Grade" text, "SiP Grade" text, "SIP Grade (FTA)" text, "Profession" text,
         "Temp Promotion" text, "Start of TP text","End of TP" text, "Temp Promotion Reason" text,
          "Temp Promotion Grade" text, "Date of Birth" text, "Age" text, "Entry Date" text, "Initial start date" text,
           "Date to CS" text, "Years in CS" text, "Organizational Unit" text,"Organizational Unit Text" text,
               "Pay Scale Area" text, "Pay Scale Group" text, "Pay Scale Level" text, "Pay Scale Type" text,
                "Payroll Area" text,"Personnel Subarea" text, "Position" text, "Position Text" text, "Weekly Hrs" text,
                 "Work schedule" text, "Work schedule rule" text, "Cost Code" text, "Cost Centre Name" text,
                  "Admin/Prog" text, "Directorate" text, "Line of Business" text, "Sub-Directorate Group" text,
                  "Line Manager PID" text, "Line Manager Name" text, "Line Manager Grade" text,
                   "Line Manager GSI Address" text, "Chief Position" text, "FT/PT" text, "Gender" text,
                   "Marital status" text, "Ethnic Origin" text,"Ethnicity Status" text, "Ethnicity Updated" text,
                    "National Identity" text, "Nationality" text, "Disability" text, "Disability Status" text,
                     "Disabilty Updated" text, "Sexual Orientation Updated" text, "Sexual Orientation" text,
                      "Sexual Orientation Category" text, "Religion Or Belief Updated" text, "Religion Or Belief" text,
                       "Religion Or Belief Category" text, "Employment Status" text, "Partial retirement date" text,
                        "FTE" text,"Absence Start" text, "Half Pay Start" text, "Pension Rate Start" text,
                         "Pension Rate End" text, "No Pay Date" text, "Absence End" text, "Type of Pay" text,
                          "Redeployment Status" text, "PreSurplus Start Date" text, "Redeployment Start Date" text,
                           "Surplus start Date" text, "BP Pack Dir" text, "BU Breakdown" text, "Distribution BU" text,
                            "SIP" text, "GSI Address" text, "Annual salary" text, "NINO" text)''')

data_file = open("data.csv")
rows = csv.reader(data_file)
next(rows)
cursor.executemany(
    "INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"
    "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
    rows)

connection.commit()
connection.close()
