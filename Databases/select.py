import sqlite3

connection=sqlite3.connect("student_record.db")

cursor=connection.cursor()

query="""SELECT Names,Marks FROM students"""
cursor.execute(query)

Names_of_students= cursor.fetchall()

for names,marks in Names_of_students:
    print(names,marks) #Burcu 100,Ayşe 90,Ali 60

print()   

#*******************************#
names_of_students2 = cursor.fetchone()

while True:
    row=cursor.fetchone()
    if row==None:
        break
    print(row)  #First item 1-Burcu-100-A

    
    