import sqlite3

db=sqlite3.connect("student_record.db")
cursor=db.cursor()


query="""SELECT DeptName FROM Student_Table INTERSECT SELECT DeptName FROM Teacher_Table"""
cursor.execute(query)

records=cursor.fetchall()

for record in records:
    print(record)

db.commit()
db.close()