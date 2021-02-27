import smtplib
import traceback

def send_mail(sender, receiver):
    message = """From: No Reply {}>
    To: Contact <{}>
    Subject: Test Email

    This is a test e-mail message.
    """.format(sender, receiver)

    result = ''
    smtpObj = None
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, message)         
        result = 'Successfully sent email'
    except Exception as error:
        result = traceback.format_exc()
    if smtpObj is not None:
        smtpObj.quit()
    return result
