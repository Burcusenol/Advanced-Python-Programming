import sqlite3

db=sqlite3.connect('student_record.db')
cursor=db.cursor()


query="""SELECT Names FROM  students WHERE Names GLOB 'A*' """

cursor.execute(query)

names=cursor.fetchall()


for name in names:
    print(name)  #Büyük A ile başlayan isimler // (*sa) -->sa ile bitenler
    

#'?er*' -->başı önemli değil içinde er olanlar
# '*[1-9]* -->içinde sayılar geçen [A-D]-->içinde a-d geçenler


