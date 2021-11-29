import sqlite3

db=sqlite3.connect("student_record.db")
cursor=db.cursor()

query="""ALTER TABLE Teacher_Table RENAME TO teacher_record"""


query2="""ALTER TABLE teacher_record ADD COLUMN email"""
cursor.execute(query2)

db.commit()
db.close()