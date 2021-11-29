import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT DISTINCT Names,Marks From students"""
cursor.execute(query)

names=cursor.fetchall()

for name,mark in names:
    print(name,mark)
    
db.commit()
db.close()
