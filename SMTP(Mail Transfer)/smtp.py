#POP3:uses port 110  
#IMAP: uses port 143 
#MIME: allows users to send diferent kinds of files over the internet,such as video,images,etc.

import smtplib 

host='smtp.gmail.com'
port=587
message="Hey I have received a new email message using Python"

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
    connection.sendmail(_from,_to,message)
    connection.quit()
except:
    print("Connection error")
    

