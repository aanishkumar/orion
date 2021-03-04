import csv
import datetime
import os
from faker import Faker

if __name__ == '__main__':
    no_of_records = int(os.getenv("NO_OF_RECORDS", 2))
    headers = ["PIDNo", "Full Name", "Name", "First Name", "Last Name", "Appointed (ERP) Office Name",
               "Appointed (ERP) Office Town", "Appointed (ERP) Office Postcode", "Appointed (ERP) Office GOR",
               "OfficeLat", "OfficeLong", "Steps Code", "Contract Type", "Employee Group", "Perm/Temp", "FTA End Date",
               "Grade", "HMRC Grade", "SiP Grade", "SIP Grade (FTA)"]
    generate_data(no_of_records, headers)


def generate_data(records, header_names):
    with open("data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=header_names)
        writer.writeheader()
        for _ in range(records):
            write_row(writer)


def write_row(writer):
    fake = Faker('en_GB')
    full_name = fake.name()
    name = full_name.split(" ")
    first_name = name[0]
    last_name = name[1]
    writer.writerow({

        "PIDNo": fake.random_number(),
        "Full Name": full_name,
        "Name": full_name,
        "First Name": first_name,
        "Last Name": last_name,
        "Appointed (ERP) Office Name": fake.company(),
        "Appointed (ERP) Office Town": fake.city(),
        "Appointed (ERP) Office Postcode": fake.postcode(),
        "Appointed (ERP) Office GOR": fake.city(),
        "OfficeLat": fake.latitude(),
        "OfficeLong": fake.longitude(),
        "Steps Code": fake.job(),
        "Contract Type": fake.job(),
        "Employee Group": fake.job(),
        "Perm/Temp": "Permanent",
        "FTA End Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
        "Grade": fake.job(),
        "HMRC Grade": fake.job(),
        "SiP Grade": fake.job(),
        "SIP Grade (FTA)": fake.job(),
    })
