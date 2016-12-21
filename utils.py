import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import settings
import os


class Email:

    @classmethod
    def send(cls):

        print('Sending code snippet in Email...')

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = settings.EMAIL_SUBJECT
        msg['to'] = settings.RECEIVER_EMAIL

        with open(os.path.join('code_snippet', 'gtm.txt'), 'r') as f:
            code_snippet = f.read()
            f.close()

        # Record the MIME type text/plain
        text = MIMEText(code_snippet, 'plain')
        msg.attach(text)

        # Send the message via SMTP server.
        try:
            server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
        except smtplib.socket.gaierror as error:
            raise Exception('Invalid HOST or PORT for SMTP configuration: Original Message: %s' % (error))

        server.starttls()

        try:
            server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        except smtplib.SMTPAuthenticationError as error:
            raise Exception('Invalid username or password for SMTP configuration: Original Message: %s' % (error))
            server.quit()

        # returns nothing if sent successfully.
        sent = server.sendmail(settings.SENDER_EMAIL, settings.RECEIVER_EMAIL, msg.as_string())
        if sent:
            print(sent)

        server.quit()
