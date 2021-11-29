import sqlite3

db=sqlite3.connect("student_record.db")
cursor=db.cursor()

query="""SELECT Names,substr(Names,2,4) FROM students"""

query2="""SELECT Names,Trim(Names,'a') FROM students WHERE Id=2"""

query3="""SELECT Names,Upper(Names) FROM students"""

query3="""SELECT Names, instr(Names,'a') FROM students"""

cursor.execute(query3)

records=cursor.fetchall()

for record in records:
    print(record)

db.commit()
db.close()