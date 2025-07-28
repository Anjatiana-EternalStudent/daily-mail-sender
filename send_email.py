from dotenv import load_dotenv
import smtplib, os, datetime
from email.mime.text import MIMEText
from get_quote import get_random_quote

load_dotenv()

citation = get_random_quote()
subject = f"Today is {datetime.date.today()}"
body = f"""
    Hello, here is your daily quote

    {citation}
"""
sender = os.getenv("EMAIL")
recipients = os.getenv("RECIPIENTS").split(",")
password = os.getenv("MDP")

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)