import sqlite3 as dbms

con = dbms.connect('abc.db')

cur = con.cursor()

# one time task
#cur.execute("Create Table Student (Rollno text, Stname text, Semester int, phoneno text, deptno text)")

r = 'BSDSF22A027'
n = 'HAJRA'
d = 'DS'
s = 6

cur = con.execute("Insert into Student (semester, rollno, stname, deptno) values(?,?,?,?)", (s, r,n,d))
con.commit()

print(cur.rowcount)

cur.execute("SELECT rollno, stname, deptno, semester FROM student")
for row in cur:
    print(row)

cur.close()
con.close()
