import pandas
import datetime as dt
import smtplib
import random

# Constants
# Info for logging in. Replace to get it working.
USER = 'TEST'
PASSWORD = 'TEST'

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Read CSV
csv = pandas.read_csv('birthdays.csv')

current_date = dt.datetime.now()
birthdays = csv.loc[(csv['day'] == current_date.day) & (csv['month'] == current_date.month)]
if len(birthdays) > 0:
  print("Birthdays found.")
  emails = birthdays['email'].to_list()
  names = birthdays['name'].to_list()
  for index in range(len(emails)):
    letter_number = random.randint(1,3)
    file = open(f"letter_templates/letter_{letter_number}.txt")
    birthday_wish = file.read().replace("[NAME]", names[index])
    msg = f"Subject: Happy Birthday\n\n{birthday_wish}"
    mail = smtplib.SMTP(host='smtp.gmail.com')
    mail.starttls()
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, emails[index], msg)
    mail.close()
    file.close()
  print("Emails were sent.")