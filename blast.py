import os
import smtplib
from email.message import EmailMessage

# set up email and password variables #
email_address = os.environ.get('KEVIN_EMAIL')
email_password = os.environ.get('py_email_blast')

# my contact list to be email blasted #
contacts = ['email@gmail.com', ]

# run a for loop to email each contact directly #
for contact in contacts:
    msg = EmailMessage()
    msg['Subject'] = 'Kevin Chancey / Web Developer'
    msg['From'] = email_address
    msg['To'] = contact
    msg.set_content('Hi - My name is Kevin and I am a full-stack developer. I was hoping this email reached the hiring manager or could be forwarded to them please?\n\nCurrently, I am a freelance programmer and in search of a long-term career and wanted to see if your company had any open entry level positions for a software engineer or web developer. If so, I would love to chat!\n\nI have attached my cover letter and resume.\n\n\nThanks,\nKevin Chancey\n(000)000-0000\nEmail@Gmail.com\nhttp://kevinchancey.xyz/')

# attach my resume & cover letter to the email #
    files = ['Kevin_Chancey_Letter.pdf','Kevin_Chancey_Resume.pdf']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# login to my email and send! #
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
