#HTML Message
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host='smtp.gmail.com'
port=587
message="<h1>Hey I have received a new email message using Python<h1>"

userName='abcde@gmail.com'
password='abcde12'

try:
    connection=smtplib.SMTP(host,port)
    print("Connection succesful")
    connection.ehlo() #empty server
    connection.starttls()
    _from=userName
    _to=[userName,'abdc@gmail.com'] #2. bcc
    connection.login(userName,password)
    # connection.sendmail(_from,_to,message)
    # connection.quit()
except:
    print("Connection error")
    
    
tmessage=MIMEMultipart("alternative")
tmessage['Subject']="Html Message"
tmessage['From']=_from
tmessage["To"]=_to

plain_message="This is a plain message"
html_message="""<html><body><h1>Students Marks</h1><p>These are the students Marks</p></body></html>"""
msg=MIMEText(html_message,"html")
msg2=MIMEText(plain_message,"plain")
tmessage.attach(msg)
tmessage.attach(msg2)

connection.sendmail(_from,_to,message)
connection.quit()