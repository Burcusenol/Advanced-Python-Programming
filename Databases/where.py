import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT Names From students WHERE Id=2 OR Names='Burcu'"""
cursor.execute(query)

names=cursor.fetchall()

for name in names:
    print(name)  #Ayşe-Burcu

