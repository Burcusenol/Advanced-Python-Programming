import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

host="smpt@gmail.com"
port=587

email_from="abcde@gmail.com"
email_password="abcde12"
email_to="abcde@gmail.com"
email_subject="Student Data"

message=MIMEMultipart()
message['From']=email_from
message["To"]=email_to
message["Subject"]=email_subject

plain_text="The file gives information about students"

message.attach(MIMEBase(plain_text,"plain"))

filename="student_names.txt"
openfile=open(filename,"rb")

mimref=MIMEBase('application','octect_stream')
mimref.set_payload((openfile.read()))
encoders.encode_base64(mimref)
mimref.add_header('Content-Disposition','openfile;filename= '+filename)
message.attach(mimref)

host=smtplib.SMTP(host,port)
host.starttls()
host.login(email_from,email_password)
host.sendmail(email_from,email_to,message.as_string())
host.quit()

