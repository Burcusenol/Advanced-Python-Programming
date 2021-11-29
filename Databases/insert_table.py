import sqlite3

connection=sqlite3.connect("student_record.db")
cursor=connection.cursor()
cursor.execute("""INSERT INTO students(Id,Names,Marks,Grades) VALUES(?,?,?,?)""",(3,"Ali","60","C"))
connection.commit()

connection.close()