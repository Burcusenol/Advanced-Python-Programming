import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT Names FROM students ORDER BY Names ASC"""

cursor.execute(query)
names=cursor.fetchall()

for name in names:
    print(name)  #Ali,Ayşe,Burcu