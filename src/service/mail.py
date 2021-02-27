from smtplib import SMTP
from email.mime.text import MIMEText
import traceback

def send_mail(sender, receiver):
    message = MIMEText('<h3>Message envoyé depuis le formulaire de contact.</h3><p>waadupp</p>', 'html')
    message['Subject'] = 'Message envoyé depuis le serveur.'
    message['From'] = sender
    message['To'] = receiver
    message['Content-Type'] = 'text/html; charset=UTF-8'
    message['X-Mailer: Python']

    result = ''
    smtp = None
    try:
        smtp = SMTP('localhost')
        smtp.sendmail(sender, receiver, message.as_string())         
        result = 'Successfully sent email'
    except Exception as error:
        result = error.args[1]
    if smtp is not None:
        smtp.quit()
    return result
