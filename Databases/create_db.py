import sqlite3
from _sqlite3 import *
try:
    database=sqlite3.connect('student_record.db')
    print("Connection Succesful")
    database.execute("""CREATE TABLE students(
        Id INT PRIMARY KEY NOT NULL,
        Names TEXT NOT NULL,
        Marks TEXT NOT NULL,
        Grades TEXT NOT NULL)""")
    database.close()
except:
    print("Connection Error")
