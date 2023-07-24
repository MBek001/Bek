import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
n=int(input())

for i in range(n):
    sender_email = 'mmm857436@gmail.com'
    reciever_email = 'abdullohergashev124@gmail.com'
    subject = 'senga Sovet'
    message = f'qizla bn kop gaplawmasdan dars qil'

    # SMTP server configuration for gmail
    smpt_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mmm857436@gmail.com'
    smtp_password = 'cfjflenmbkpjwduf'

    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['from'] = sender_email
    email_message['To'] = reciever_email
    email_message['Subject'] = subject

    email_message.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smpt_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)


print('Success')