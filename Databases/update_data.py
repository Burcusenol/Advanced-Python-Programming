import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""UPDATE students SET Marks='89',Grades='B' WHERE Id=11"""
query2="""UPDATE students SET Marks='99',Grades='A' WHERE Id=7"""

cursor.execute(query)
cursor.execute(query2)
db.commit()
db.close()
