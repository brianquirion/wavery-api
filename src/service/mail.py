from smtplib import SMTP
from email.mime.text import MIMEText
import traceback

def send_mail(sender: str, receiver: str, reply_to: str, subject: str, body: str):
    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message['Reply-To'] = reply_to
    message['Content-Type'] = 'text/html; charset=UTF-8'
    message['X-Mailer: Python']

    smtp = SMTP('localhost')
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()
