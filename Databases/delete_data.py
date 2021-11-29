import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()


query1="""DELETE FROM Names WHERE Name LIKE '%ren%'"""
cursor.execute(query1)

db.commit()
db.close()
