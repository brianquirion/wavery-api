import smtplib

def send_mail(sender, receiver):
    message = """From: No Reply {}>
    To: Contact <{}>
    Subject: Test Email

    This is a test e-mail message.
    """.format(sender, receiver)

    result = ''
    smtpObj = smtplib.SMTP('localhost')
    try:
        smtpObj.sendmail(sender, receiver, message)         
        result = 'Successfully sent email'
    except SMTPException:
        result = 'Error: unable to send email'
    smtpObj.quit()
