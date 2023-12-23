import datetime as dt
import pandas as pd
import random
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "your_email_address"
GMAIL_PASSWORD = "your password"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(GMAIL_USER, GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_USER,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
    print("Birthday email sent successfully.")
else:
    print("No birthdays today.")
