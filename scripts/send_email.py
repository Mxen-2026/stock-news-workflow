import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.qq.com'
smtp_port = 587  # or 465 for SSL
sender_email = 'your_email@qq.com'
sender_password = 'your_password'
receiver_email = 'receiver_email@example.com'

# Create email content
subject = 'Email Report'
body = 'This is the email report content.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure
    server.login(sender_email, sender_password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully')

except Exception as e:
    print(f'Error: {e}')

finally:
    server.quit()