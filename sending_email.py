import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL_ADDRESS = "umosengodwin568@gmail.com"
EMAIL_PASSWORD = "123456789ten"
RECIEVER_EMAIL_ADDRESS_2 = "godwinsenwin@gmail.com"

msg = EmailMessage()
msg['Subject']= 'Testing the subject of the mail sent by python code'
msg['From']= SENDER_EMAIL_ADDRESS
msg['To']=RECIEVER_EMAIL_ADDRESS_2 
msg.set_content('To verify if the emaill would be deliver to the above address code.')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.starttls()
    smtp.login(SENDER_EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

'''with open ('the_file.txt') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

#me == the sender's address emaill
# you == the recipient or reciever email address

msg['From'] = 'godwinsenwin@gmail.com'
msg['To'] ='umosengodwin568@gmail.com'
msg['Subject'] = f"The contents of {'the_file.txt'}"

#send the message via SMP server email
server = smtplib.SMTP('smtp.gmail.com',587)
server.send_message(msg)
server.quit()'''