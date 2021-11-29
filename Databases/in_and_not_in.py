import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()

query="""SELECT Names,Marks FROM students WHERE Id NOT IN(4,5,7,9) ORDER BY Names ASC"""

cursor.execute(query)

names=cursor.fetchall()

for name in names:
    print(name)  #Ali,Ayşe,Sena,Yıldız->IN /NOT IN->1,2,6,8,10,11
    
db.commit()
db.close()
    
