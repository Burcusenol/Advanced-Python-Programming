import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT DISTINCT Names FROM  students WHERE Names LIKE 'a%' """

cursor.execute(query)

names=cursor.fetchall()


for name in names:
    print(name)  #Ali,Ayşe 
    
#'%a' --> names and with it
#'%ni% --> içinde ni geçen