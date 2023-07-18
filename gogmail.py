import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['Subject']=subject
    msg['to']=to

    user="pmgroup.alert@gmail.com"
    msg['from']=user
    password="xknvmrhrulljsond"

    sever=smtplib.SMTP("smtp.gmail.com",587)
    sever.starttls()
    sever.login(user,password)
    sever.send_message(msg)

    sever.quit()
    
