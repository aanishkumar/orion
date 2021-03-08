import csv
import datetime
import os
from faker import Faker


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
        "Perm/Temp": fake.random.choice(["Permanent", "Contract"]),
        "FTA End Date": date(fake),
        "Grade": fake.job(),
        "HMRC Grade": fake.job(),
        "SiP Grade": fake.job(),
        "SIP Grade (FTA)": fake.job(),

        "Profession": fake.job(),
        "Temp Promotion": fake.job(),
        "Start of TP": date(fake),
        "End of TP": date(fake),
        "Temp Promotion Reason": fake.job(),
        "Temp Promotion Grade": fake.job(),
        "Date of Birth": fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115),
        "Age": fake.random.randint(1, 100),
        "Entry Date": date(fake),
        "Initial start date": date(fake),
        "Date to CS": date(fake),
        "Years in CS": fake.random.randint(1, 20),
        "Organizational Unit": fake.job(),
        "Organizational Unit Text": fake.job(),
        "Pay Scale Area": fake.job(),
        "Pay Scale Group": fake.job(),
        "Pay Scale Level": fake.job(),
        "Pay Scale Type": fake.job(),
        "Payroll Area": fake.job(),
        "Personnel Subarea": fake.job(),
        "Position": fake.job(),
        "Position Text": fake.job(),
        "Weekly Hrs": fake.random.choice(["40", "35", "10"]),
        "Work schedule": work_schedule(fake),
        "Work schedule rule": work_schedule(fake),
        "Cost Code": fake.random_number(),
        "Cost Centre Name": fake.address(),
        "Admin/Prog": fake.random.choice(["Admin", "Programmer"]),
        "Directorate": fake.job(),
        "Line of Business": fake.job(),

        "Sub-Directorate Group": fake.job(),
        "Line Manager PID": fake.random_number(),
        "Line Manager Name": fake.name(),
        "Line Manager Grade": fake.job(),
        "Line Manager GSI Address": fake.address(),
        "Chief Position": fake.job(),
        "FT/PT": fake.random.choice(["FT", "PT"]),
        "Gender": fake.random.choice(["Male", "Female"]),
        "Marital status": fake.random.choice(["Single", "Married"]),
        "Ethnic Origin": ethnic_origin(fake),
        "Ethnicity Status": ethnic_origin(fake),
        "Ethnicity Updated": ethnic_origin(fake),
        "National Identity": nationality(fake),
        "Nationality": nationality(fake),
        "Disability": "None",
        "Disability Status": "No Disability",
        "Disabilty Updated": "None",
        "Sexual Orientation Updated": sexual_orientation(fake),
        "Sexual Orientation": sexual_orientation(fake),
        "Sexual Orientation Category": sexual_orientation(fake),
        "Religion Or Belief Updated": religion(fake),
        "Religion Or Belief": religion(fake),
        "Religion Or Belief Category": religion(fake),
        "Employment Status": employment_status(fake),
        "Partial retirement date": date(fake),
        "FTE": fake.job(),
        "Absence Start": date(fake),
        "Half Pay Start": date(fake),
        "Pension Rate Start": date(fake),
        "Pension Rate End": date(fake),
        "No Pay Date": date(fake),
        "Absence End": date(fake),
        "Type of Pay": fake.job(),
        "Redeployment Status": fake.job(),
        "PreSurplus Start Date": date(fake),
        "Redeployment Start Date": date(fake),
        "Surplus start Date": date(fake),
        "BP Pack Dir": fake.job(),
        "BU Breakdown": fake.job(),
        "Distribution BU": fake.job(),
        "SIP": fake.job(),
        "GSI Address": fake.address(),
        "Annual salary": fake.random_number(),
        "NINO": fake.random_number(),

    })


def work_schedule(fake):
    return fake.random.choice(["Full-Time", "Part-Time", "Fixed", "Flextime"])


def nationality(fake):
    return fake.random.choice(["United Kingdom", "Italian", "German"])


def ethnic_origin(fake):
    return fake.random.choice(["Mixed or Multiple ethnic groups", "White", "Asian or Asian British",
                               "Black, African, Caribbean or Black British", "Other ethnic group"])


def religion(fake):
    return fake.random.choice(
        ["Polytheism", "Monotheism", "Atheism", "Animism", "Totemism"])


def sexual_orientation(fake):
    return fake.random.choice(["Heterosexual", "Homosexual", "German"])


def employment_status(fake):
    return fake.random.choice(["worker", "employee", "self-employed and contractor",
                               "director", "office holder"])


def date(fake):
    return fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1))


if __name__ == '__main__':
    no_of_records = int(os.getenv("NO_OF_RECORDS", 2))
    headers = ["PIDNo", "Full Name", "Name", "First Name", "Last Name", "Appointed (ERP) Office Name",
               "Appointed (ERP) Office Town", "Appointed (ERP) Office Postcode", "Appointed (ERP) Office GOR",
               "OfficeLat", "OfficeLong", "Steps Code", "Contract Type", "Employee Group", "Perm/Temp", "FTA End Date",
               "Grade", "HMRC Grade", "SiP Grade", "SIP Grade (FTA)", "Profession", "Temp Promotion", "Start of TP",
               "End of TP", "Temp Promotion Reason", "Temp Promotion Grade", "Date of Birth", "Age", "Entry Date",
               "Initial start date", "Date to CS", "Years in CS", "Organizational Unit", "Organizational Unit Text",
               "Pay Scale Area", "Pay Scale Group", "Pay Scale Level", "Pay Scale Type", "Payroll Area",
               "Personnel Subarea", "Position", "Position Text", "Weekly Hrs", "Work schedule", "Work schedule rule",
               "Cost Code", "Cost Centre Name", "Admin/Prog", "Directorate", "Line of Business",
               "Sub-Directorate Group", "Line Manager PID", "Line Manager Name", "Line Manager Grade",
               "Line Manager GSI Address", "Chief Position", "FT/PT", "Gender", "Marital status", "Ethnic Origin",
               "Ethnicity Status", "Ethnicity Updated", "National Identity", "Nationality", "Disability",
               "Disability Status", "Disabilty Updated", "Sexual Orientation Updated", "Sexual Orientation",
               "Sexual Orientation Category", "Religion Or Belief Updated", "Religion Or Belief",
               "Religion Or Belief Category", "Employment Status", "Partial retirement date", "FTE", "Absence Start",
               "Half Pay Start", "Pension Rate Start", "Pension Rate End", "No Pay Date", "Absence End", "Type of Pay",
               "Redeployment Status", "PreSurplus Start Date", "Redeployment Start Date", "Surplus start Date",
               "BP Pack Dir", "BU Breakdown", "Distribution BU", "SIP", "GSI Address", "Annual salary", "NINO"]
    generate_data(no_of_records, headers)
