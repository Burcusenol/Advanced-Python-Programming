import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()


query="""SELECT Id,Names FROM students LIMIT 3 OFFSET 4 """

cursor.execute(query)

names=cursor.fetchall()

for name in names:
    print(name)  #♦5,6,7. kayıtları getirir
    