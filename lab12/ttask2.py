import sqlite3
conn = sqlite3.connect('employees.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS dept (
               deptno INTEGER PRIMARY KEY,
               dname TEXT,
               location TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS emp (
               empno INTEGER PRIMARY KEY,
               ename TEXT,
               job TEXT,
               mgr INTEGER,
               hiredate TEXT,
               sal REAL,
               comm REAL,
               deptno INTEGER,
               FOREIGN KEY (deptno) REFERENCES dept(deptno))''')
cur.execute('''CREATE TABLE IF NOT EXISTS salgrade (
               grade INTEGER PRIMARY KEY,
               losal REAL,
               hisal REAL)''')
def menu():
    print("Menu:")
    print("a) Add Employee")
    print("s) Search Employee")
    print("d) Delete Employee")
    print("l) List All Employees")
    print("e) Edit Employee")
    print("n) Edit Employee Name")
    print("j) Edit Employee Job")
    print("m) Edit Employee Manager")
    print("h) Edit Employee Hire Date")
    print("sl) Edit Employee Salary")
    print("c) Edit Employee Commission")
    print("q) Quit")
def add_employee(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    cur.execute("INSERT INTO emp (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (empno, ename, job, mgr, hiredate, sal, comm, deptno))
    conn.commit()
def search_employee_by_name(ename):
    cur.execute("SELECT * FROM emp WHERE ename=?", (ename,))
    result = cur.fetchall()
    return result
def delete_employee(empno):
    cur.execute("DELETE FROM emp WHERE empno=?", (empno,))
    conn.commit()
def list_all_employees():
    cur.execute("SELECT * FROM emp")
    result = cur.fetchall()
    return result
def edit_employee(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    cur.execute("UPDATE emp SET ename=?, job=?, mgr=?, hiredate=?, sal=?, comm=?, deptno=? WHERE empno=?",
                (ename, job, mgr, hiredate, sal, comm, deptno, empno))
    conn.commit()
def edit_employee_name(empno, ename):
    cur.execute("UPDATE emp SET ename=? WHERE empno=?", (ename, empno))
    conn.commit()
def edit_employee_job(empno, job):
    cur.execute("UPDATE emp SET job=? WHERE empno=?", (job, empno))
    conn.commit()
def edit_employee_manager(empno, mgr):
    cur.execute("UPDATE emp SET mgr=? WHERE empno=?", (mgr, empno))
    conn.commit()
def edit_employee_hire_date(empno, hiredate):
    cur.execute("UPDATE emp SET hiredate=? WHERE empno=?", (hiredate, empno))
    conn.commit()
def edit_employee_salary(empno, sal):
    cur.execute("UPDATE emp SET sal=? WHERE empno=?", (sal, empno))
    conn.commit()
def edit_employee_commission(empno, comm):
    cur.execute("UPDATE emp SET comm=? WHERE empno=?", (comm, empno))
    conn.commit()
def main():
    while True:
        menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            break
        elif choice == 'a':
            empno = int(input("Enter employee number: "))
            ename = input("Enter employee name: ")
            job = input("Enter employee job: ")
            mgr = int(input("Enter employee manager's employee number: "))
            hiredate = input("Enter employee hire date (YYYY-MM-DD): ")
            sal = float(input("Enter employee salary: "))
            comm = float(input("Enter employee commission: "))
            deptno = int(input("Enter employee department number: "))
            add_employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
            print("Employee added successfully.")
        elif choice == 's':
            ename = input("Enter employee name to search: ")
            result = search_employee_by_name(ename)
            if result:
                print("Employee found:", result)
            else:
                print("Employee not found.")
        elif choice == 'd':
            empno = int(input("Enter employee number to delete: "))
            delete_employee(empno)
            print("Employee deleted successfully.")
        elif choice == 'l':
            result = list_all_employees()
            if result:
                for row in result:
                    print(row)
            else:
                print("No employees found.")
        elif choice == 'e':
            empno = int(input("Enter employee number to edit: "))
            ename = input("Enter new employee name: ")
            job = input("Enter new employee job: ")
            mgr = int(input("Enter new employee manager's employee number: "))
            hiredate = input("Enter new employee hire date (YYYY-MM-DD): ")
            sal = float(input("Enter new employee salary: "))
            comm = float(input("Enter new employee commission: "))
            deptno = int(input("Enter new employee department number: "))
            edit_employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
            print("Employee edited successfully.")
        elif choice == 'n':
            empno = int(input("Enter employee number to edit name: "))
            ename = input("Enter new employee name: ")
            edit_employee_name(empno, ename)
            print("Employee name edited successfully.")
        elif choice == 'j':
            empno = int(input("Enter employee number to edit job: "))
            job = input("Enter new employee job: ")
            edit_employee_job(empno, job)
            print("Employee job edited successfully.")
        elif choice == 'm':
            empno = int(input("Enter employee number to edit manager: "))
            mgr = int(input("Enter new manager's employee number: "))
            edit_employee_manager(empno, mgr)
            print("Employee manager edited successfully.")
        elif choice == 'c':
            empno = int(input("Enter employee number to edit manager: "))
            mgr = int(input("Enter new manager's employee number: "))
            edit_employee_manager(empno, mgr)
            print("Employee commision edited successfully.")
        elif choice == 'h':
            empno = int(input("Enter employee number to edit hire date: "))
            hiredate = input("Enter new employee hire date (YYYY-MM-DD): ")
            edit_employee_hire_date(empno, hiredate)
            print("Employee hire date edited successfully.")
        elif choice == 'sl':
            empno = int(input("Enter employee number to edit salary: "))
            sal = float(input("Enter new employee salary: "))
            edit_employee_salary(empno, sal)
            print("Employee salary edited successfully.")
        elif choice == 's':
            ename = input("Enter employee name to search: ")
            result = search_employee_by_name(ename)
            if result:
                print("Employee found:", result)
            else:
                print("Employee not found.")
        elif choice == 'd':
            empno = int(input("Enter employee number to delete: "))
            delete_employee(empno)
            print("Employee deleted successfully.")
        elif choice == 'l':
            result = list_all_employees()
            if result:
                for row in result:
                    print(row)
            else:
                print("No employees found.")
        elif choice == 'e':
            empno = int(input("Enter employee number to edit: "))
            ename = input("Enter new employee name: ")
            job = input("Enter new employee job: ")
            mgr = int(input("Enter new manager's employee number: "))
            hiredate = input("Enter new hire date (YYYY-MM-DD): ")
            sal = float(input("Enter new salary: "))
            comm = float(input("Enter new commission: "))
            deptno = int(input("Enter new department number: "))
            edit_employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
            print("Employee edited successfully.")
        else:
            print("Invalid choice. Please try again.")

        conn.close()
main()