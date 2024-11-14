Python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the email sender and recipient addresses
sender_email = "phishing@example.com"
recipient_email = "victim@example.com"

# Create the email subject and body
subject = "Important Notice from Your Bank"
body = """

Dear valued customer,

We have recently detected suspicious activity on your account. To ensure the security of your funds, we need you to confirm your personal information by clicking on the link below.

Please click here to confirm your information.

Thank you for your cooperation.

Sincerely,
Your Bank
"""

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body,   
 'plain'))

# Connect to the SMTP server and send the email
server = smtplib.SMTP('smtp.gmail.com',   
 587)
server.starttls()
server.login(sender_email, 'password')
server.sendmail(sender_email, recipient_email, msg.as_string())
server.quit()