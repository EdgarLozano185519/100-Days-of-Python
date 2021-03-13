from twilio.rest import Client
import requests
import smtplib
from decouple import config

TWILIO_SID = config('TWILIO_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = config('FROM')
TWILIO_VERIFIED_NUMBER = config('TO')
FROM_EMAIL = config('FROM_EMAIL')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')
SMTP_ADDR = "smtp.gmail.com"

class NotificationManager:
  def __init__(self):
    self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  
  def send_sms(self, message):
    message = self.client.messages.create(
      body=message,
      from_=TWILIO_VIRTUAL_NUMBER,
      to=TWILIO_VERIFIED_NUMBER,
    )
    # Prints if successfully sent.
    print(message.sid)
  
  def send_emails(self, message, emails_list):
    mail = smtplib.SMTP(host=SMTP_ADDR)
    mail.starttls()
    mail.login(FROM_EMAIL, EMAIL_PASSWORD)
    for email in emails_list:
      mail.sendmail(FROM_EMAIL, email, message)
    print("Emails sent.")
    mail.close()

