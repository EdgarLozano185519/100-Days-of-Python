import smtplib
import datetime as dt
import random

# Constants
# Info for logging in. Replace to get it working.
USER = 'TEST'
PASSWORD = 'TEST'

current_date = dt.datetime.now()
if current_date.weekday() == 2:
  print("Sending email.")
  mail = smtplib.SMTP(host='smtp.gmail.com')
  mail.starttls()
  mail.login(USER, PASSWORD)
  msg = "Subject: Quote of The Day\n\n"
  file = open("quotes.txt", )
  quote = random.choice(file.readlines()).split('-')
  msg += quote[0]
  msg += "\n- "+quote[1]
  mail.sendmail(USER, "lozano.edgar94@gmail.com", msg)
  mail.close()
  file.close()
  print("Message sent.\nMessage was sent with following content:\n"+msg)