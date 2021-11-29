import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT AVG(Marks),COUNT(Names),MAX(Id),MIN(Id),SUM(Id) FROM  students"""

cursor.execute(query)

names=cursor.fetchall()


for name in names:
    print(name)