import sqlite3

db=sqlite3.connect("student_record.db")
cursor=db.cursor()

query="""SELECT round(47.976799,-1)"""

cursor.execute(query)

randoms=cursor.fetchall()

for random in randoms:
    print(random)
    

db.commit()
db.close()