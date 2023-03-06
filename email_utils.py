from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from pathlib import Path


def send_email(receivers, subject, message, attachment_filepath):
    """
    This is currently set to only send from joerosborne@gmail.com\n
    receivers - can be a list or a str\n
    subject - str\n
    message - str\n
    attachment_filepath - str\n
    """

    port = 465
    sender_email = 'example@gmail.com'
    app_password = 'app_password'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email

    msg.attach(MIMEText(message, 'plain'))
    part = MIMEBase('application', "octet-stream")

    with open(attachment_filepath, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename={}'.format(Path(attachment_filepath).name))
    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receivers, msg.as_string())
    server.quit()

    return print('Email Sent')


def send_email_no_attachment(receivers, subject, message):
    """
    This is currently set to only send from joerosborne@gmail.com\n
    receivers - can be a list or a str\n
    subject - str\n
    message - str\n
    """

    port = 465
    sender_email = 'example@gmail.com'
    app_password = 'app_password'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receivers, msg.as_string())
    server.quit()

    return print('Email Sent')

if __name__ == '__main__':

    send_email_no_attachment('joerosborne@gmail.com', 'hey', 'yeet')
