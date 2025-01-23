import sqlite3 as dbms

con = dbms.connect('abc.db')

cur = con.cursor()

txt = "Mahmood');Delete From Student;--"

stmt = "Insert into Student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, '"+ txt +"')"

print(stmt)

cur.executescript(stmt)

con.commit()
cur.close()
con.close()