import csv
import datetime
import os
from faker import Faker


def generate_data(records, header_names):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')  # To generate phone numbers
    with open("data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=header_names)
        writer.writeheader()
        for _ in range(records):
            full_name = fake.name()
            domain_name = "@testDomain.com"
            user_id = full_name + domain_name

            writer.writerow({
                "Email Id": user_id,
                "Prefix": fake.prefix(),
                "Name": full_name,
                "Birth Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                "Phone Number": fake1.phone_number(),
                "Additional Email Id": fake.email(),
                "Address": fake.address(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Country": fake.country(),
                "Year": fake.year(),
                "Time": fake.time(),
                "Link": fake.url(),
                "Text": fake.word(),
            })


if __name__ == '__main__':
    no_of_records = int(os.getenv("NO_OF_RECORDS"))
    headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City", "State", "Country", "Year", "Time", "Link", "Text"]
    generate_data(no_of_records, headers)
    print("CSV generation complete!")
