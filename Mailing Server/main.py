import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)  # Creating the server using smtp

# Starting the smtp
server.ehlo()

with open('password.txt', 'r') as f:  # Reading password from the text files
    password = f.read()

server.starttls()  # Solves the bug....

# Logging into the server/mail account
server.login('unexpectedprogrammer@gmail.com', password)

""" Creating the message using the module """
msg = MIMEMultipart()
msg['from'] = 'Fahad'
msg['to'] = 'kacjao@spaml.de'
msg['subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'friends.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename = {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('unexpectedprogrammer@gmail.com', 'kacjao@spaml.de', text)

print(f"Mail Has Been Sent Succesfully To {msg['to']}")
