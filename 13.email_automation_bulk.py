# Set up your gmail account
# Turn on 2-step verification
# Generate app passwords --> Gmail account > Manage your Google account >
# 2-step verification and app password is on.
# simple mail transfer protocol
import csv
import smtplib
import ssl
from email.message import EmailMessage

sender = ''  # add your sender email address
password = ''  # add your app password added earlier(Gmail)

subject = ''  # subject of your email
body_message = ''  # Your body message

# connect to our outgoing mail server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

server.login(sender, password)

path = 'C:\\Users\\Louis\\Desktop\\mail.csv'
with open('mail.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        server.send_message(em)
        print("Message sent successfully!!!")

server.close()
print("Task done!!!")
