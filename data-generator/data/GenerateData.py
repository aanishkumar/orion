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
        "Absence End": date(fake),
        "Absence Start": date(fake),
        "Admin/Prog": fake.random.choice(["Admin", "Programmer"]),
        "Age": fake.random.randint(1, 100),
        "Annual salary": fake.random_number(),
        "Appointed (ERP) Office GOR": fake.city(),
        "Appointed (ERP) Office Name": fake.company(),
        "Appointed (ERP) Office Postcode": fake.postcode(),
        "Appointed (ERP) Office Town": fake.city(),
        "BP Pack Dir": fake.job(),
        "BU Breakdown": fake.job(),
        "Chief Position": fake.job(),
        "Contract Type": fake.job(),
        "Cost Centre Name": fake.address(),
        "Cost Code": fake.random_number(),
        "Date of Birth": fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115),
        "Date to CS": date(fake),
        "Directorate": fake.job(),
        "Disability Status": "No Disability",
        "Disability": "None",
        "Disabilty Updated": "None",
        "Distribution BU": fake.job(),
        "Employee Group": fake.job(),
        "Employment Status": employment_status(fake),
        "End of TP": date(fake),
        "Entry Date": date(fake),
        "Ethnic Origin": ethnic_origin(fake),
        "Ethnicity Status": ethnic_origin(fake),
        "Ethnicity Updated": ethnic_origin(fake),
        "FT/PT": fake.random.choice(["FT", "PT"]),
        "FTA End Date": date(fake),
        "FTE": fake.job(),
        "First Name": first_name,
        "Full Name": full_name,
        "GSI Address": fake.address(),
        "Gender": fake.random.choice(["Male", "Female"]),
        "Grade": fake.job(),
        "HMRC Grade": fake.job(),
        "Half Pay Start": date(fake),
        "Initial start date": date(fake),
        "Last Name": last_name,
        "Line Manager GSI Address": fake.address(),
        "Line Manager Grade": fake.job(),
        "Line Manager Name": fake.name(),
        "Line Manager PID": fake.random_number(),
        "Line of Business": fake.job(),
        "Marital status": fake.random.choice(["Single", "Married"]),
        "NINO": fake.random_number(),
        "Name": full_name,
        "National Identity": nationality(fake),
        "Nationality": nationality(fake),
        "No Pay Date": date(fake),
        "OfficeLat": fake.latitude(),
        "OfficeLong": fake.longitude(),
        "Organizational Unit Text": fake.job(),
        "Organizational Unit": fake.job(),
        "PIDNo": fake.random_number(),
        "Partial retirement date": date(fake),
        "Pay Scale Area": fake.job(),
        "Pay Scale Group": fake.job(),
        "Pay Scale Level": fake.job(),
        "Pay Scale Type": fake.job(),
        "Payroll Area": fake.job(),
        "Pension Rate End": date(fake),
        "Pension Rate Start": date(fake),
        "Perm/Temp": fake.random.choice(["Permanent", "Contract"]),
        "Personnel Subarea": fake.job(),
        "Position Text": fake.job(),
        "Position": fake.job(),
        "PreSurplus Start Date": date(fake),
        "Profession": fake.job(),
        "Redeployment Start Date": date(fake),
        "Redeployment Status": fake.job(),
        "Religion Or Belief Category": religion(fake),
        "Religion Or Belief Updated": religion(fake),
        "Religion Or Belief": religion(fake),
        "SIP Grade (FTA)": fake.job(),
        "SIP": fake.job(),
        "Sexual Orientation Category": sexual_orientation(fake),
        "Sexual Orientation Updated": sexual_orientation(fake),
        "Sexual Orientation": sexual_orientation(fake),
        "SiP Grade": fake.job(),
        "Start of TP": date(fake),
        "Steps Code": fake.job(),
        "Sub-Directorate Group": fake.job(),
        "Surplus start Date": date(fake),
        "Temp Promotion Grade": fake.job(),
        "Temp Promotion Reason": fake.job(),
        "Temp Promotion": fake.job(),
        "Type of Pay": fake.job(),
        "Weekly Hrs": fake.random.choice(["40", "35", "10"]),
        "Work schedule rule": work_schedule(fake),
        "Work schedule": work_schedule(fake),
        "Years in CS": fake.random.randint(1, 20),
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
    headers = ["Absence End",
               "Absence Start",
               "Admin/Prog",
               "Age",
               "Annual salary",
               "Appointed (ERP) Office GOR",
               "Appointed (ERP) Office Name",
               "Appointed (ERP) Office Postcode",
               "Appointed (ERP) Office Town",
               "BP Pack Dir",
               "BU Breakdown",
               "Chief Position",
               "Contract Type",
               "Cost Centre Name",
               "Cost Code",
               "Date of Birth",
               "Date to CS",
               "Directorate",
               "Disability Status",
               "Disability",
               "Disabilty Updated",
               "Distribution BU",
               "Employee Group",
               "Employment Status",
               "End of TP",
               "Entry Date",
               "Ethnic Origin",
               "Ethnicity Status",
               "Ethnicity Updated",
               "FT/PT", "Gender",
               "FTA End Date",
               "FTE",
               "First Name",
               "Full Name",
               "GSI Address",
               "Grade",
               "HMRC Grade",
               "Half Pay Start",
               "Initial start date",
               "Last Name",
               "Line Manager GSI Address",
               "Line Manager Grade",
               "Line Manager Name",
               "Line Manager PID",
               "Line of Business",
               "Marital status",
               "NINO",
               "Name",
               "National Identity",
               "Nationality",
               "No Pay Date",
               "OfficeLat",
               "OfficeLong",
               "Organizational Unit Text",
               "Organizational Unit",
               "PIDNo",
               "Partial retirement date",
               "Pay Scale Area",
               "Pay Scale Group",
               "Pay Scale Level",
               "Pay Scale Type",
               "Payroll Area",
               "Pension Rate End",
               "Pension Rate Start",
               "Perm/Temp",
               "Personnel Subarea",
               "Position Text",
               "Position",
               "PreSurplus Start Date",
               "Profession",
               "Redeployment Start Date",
               "Redeployment Status",
               "Religion Or Belief Category",
               "Religion Or Belief Updated",
               "Religion Or Belief",
               "SIP Grade (FTA)",
               "SIP",
               "Sexual Orientation Category",
               "Sexual Orientation Updated",
               "Sexual Orientation",
               "SiP Grade",
               "Start of TP",
               "Steps Code",
               "Sub-Directorate Group",
               "Surplus start Date",
               "Temp Promotion Grade",
               "Temp Promotion Reason",
               "Temp Promotion",
               "Type of Pay",
               "Weekly Hrs",
               "Work schedule rule",
               "Work schedule",
               "Years in CS"
               ]
    generate_data(no_of_records, headers)
