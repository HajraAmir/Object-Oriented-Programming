import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
class Employee:
    def __init__(self, empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno
class EmployeeDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()
    def __del__(self):
        self.conn.close()
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS emp (
            empno INTEGER PRIMARY KEY,
            ename TEXT,
            job TEXT,
            mgr INTEGER,
            hiredate TEXT,
            sal REAL,
            comm REAL,
            deptno INTEGER
        )
        """)
        self.conn.commit()
    def create_employee(self, employee):
        self.cursor.execute(
            "INSERT INTO emp (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (employee.empno, employee.ename, employee.job, employee.mgr, employee.hiredate, employee.sal, employee.comm, employee.deptno)       )
        self.conn.commit()
    def read_employee(self, empno):
        self.cursor.execute("SELECT * FROM emp WHERE empno=?", (empno,))
        row = self.cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        else:
            return None
    def update_employee(self, employee):
        self.cursor.execute(
            "UPDATE emp SET ename=?, job=?, mgr=?, hiredate=?, sal=?, comm=?, deptno=? WHERE empno=?",
            (employee.ename, employee.job, employee.mgr, employee.hiredate, employee.sal, employee.comm, employee.deptno, employee.empno)       )
        self.conn.commit()
    def delete_employee(self, empno):
        self.cursor.execute("DELETE FROM emp WHERE empno=?", (empno,))
        self.conn.commit()
class SalGrade:
    def __init__(self, grade, losal, hisal):
        self.grade = grade
        self.losal = losal
        self.hisal = hisal
class SalGradeDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()
    def __del__(self):
        self.conn.close()
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS salgrade (
            grade INTEGER PRIMARY KEY,
            losal REAL,
            hisal REAL
        )
        """)
        self.conn.commit()
    def create_salgrade(self, salgrade):
        self.cursor.execute("INSERT INTO salgrade (grade, losal, hisal) VALUES (?, ?, ?)",
                            (salgrade.grade, salgrade.losal, salgrade.hisal))
        self.conn.commit()
    def read_salgrade(self, grade):
        self.cursor.execute("SELECT * FROM salgrade WHERE grade=?", (grade,))
        row = self.cursor.fetchone()
        if row:
            return SalGrade(row[0], row[1], row[2])
        else:
            return None
    def update_salgrade(self, salgrade):
        self.cursor.execute("UPDATE salgrade SET losal=?, hisal=? WHERE grade=?",
                            (salgrade.losal, salgrade.hisal, salgrade.grade))
        self.conn.commit()
    def delete_salgrade(self, grade):
        self.cursor.execute("DELETE FROM salgrade WHERE grade=?", (grade,))
        self.conn.commit()
class EmpApp(tk.Tk):
    def __init__(self, db_file):
        super().__init__()
        self.title("Employee and SalGrade Management System")
        self.db_emp = EmployeeDB(db_file)
        self.db_salgrade = SalGradeDB(db_file)
        self.create_widgets()
    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, padx=10, pady=10)
        self.create_emp_tab()
        self.create_salgrade_tab()
    def create_emp_tab(self):
        self.emp_frame = tk.Frame(self.notebook)
        self.notebook.add(self.emp_frame, text="Employee Management")
        tk.Label(self.emp_frame, text="Emp No:").grid(row=0, column=0)
        tk.Label(self.emp_frame, text="Name:").grid(row=1, column=0)
        tk.Label(self.emp_frame, text="Job:").grid(row=2, column=0)
        tk.Label(self.emp_frame, text="Manager:").grid(row=3, column=0)
        tk.Label(self.emp_frame, text="Hire Date:").grid(row=4, column=0)
        tk.Label(self.emp_frame, text="Salary:").grid(row=5, column=0)
        tk.Label(self.emp_frame, text="Commission:").grid(row=6, column=0)
        tk.Label(self.emp_frame, text="Dept No:").grid(row=7, column=0)
        self.empno_entry = tk.Entry(self.emp_frame)
        self.empno_entry.grid(row=0, column=1)
        self.ename_entry = tk.Entry(self.emp_frame)
        self.ename_entry.grid(row=1, column=1)
        self.job_entry = tk.Entry(self.emp_frame)
        self.job_entry.grid(row=2, column=1)
        self.mgr_entry = tk.Entry(self.emp_frame)
        self.mgr_entry.grid(row=3, column=1)
        self.hiredate_entry = tk.Entry(self.emp_frame)
        self.hiredate_entry.grid(row=4, column=1)
        self.sal_entry = tk.Entry(self.emp_frame)
        self.sal_entry.grid(row=5, column=1)
        self.comm_entry = tk.Entry(self.emp_frame)
        self.comm_entry.grid(row=6, column=1)
        self.deptno_entry = tk.Entry(self.emp_frame)
        self.deptno_entry.grid(row=7, column=1)
        self.emp_buttons_frame = tk.Frame(self.emp_frame)
        self.emp_buttons_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.create_emp_button = tk.Button(self.emp_buttons_frame, text="Create", command=self.create_employee)
        self.create_emp_button.grid(row=0, column=0, pady=5)
        self.read_emp_button = tk.Button(self.emp_buttons_frame, text="Read", command=self.read_employee)
        self.read_emp_button.grid(row=0, column=1, pady=5)
        self.update_emp_button = tk.Button(self.emp_buttons_frame, text="Update", command=self.update_employee)
        self.update_emp_button.grid(row=0, column=2, pady=5)
        self.delete_emp_button = tk.Button(self.emp_buttons_frame, text="Delete", command=self.delete_employee)
        self.delete_emp_button.grid(row=0, column=3, pady=5)
        self.clear_emp_button = tk.Button(self.emp_buttons_frame, text="Clear", command=self.clear_emp_entries)
        self.clear_emp_button.grid(row=0, column=4, pady=5)
    def create_salgrade_tab(self):
        self.salgrade_frame = tk.Frame(self.notebook)
        self.notebook.add(self.salgrade_frame, text="SalGrade Management")
        tk.Label(self.salgrade_frame, text="Grade:").grid(row=0, column=0)
        tk.Label(self.salgrade_frame, text="Lowest Salary:").grid(row=1, column=0)
        tk.Label(self.salgrade_frame, text="Highest Salary:").grid(row=2, column=0)
        self.grade_entry = tk.Entry(self.salgrade_frame)
        self.grade_entry.grid(row=0, column=1)
        self.losal_entry = tk.Entry(self.salgrade_frame)
        self.losal_entry.grid(row=1, column=1)
        self.hisal_entry = tk.Entry(self.salgrade_frame)
        self.hisal_entry.grid(row=2, column=1)
        self.salgrade_buttons_frame = tk.Frame(self.salgrade_frame)
        self.salgrade_buttons_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.create_salgrade_button = tk.Button(self.salgrade_buttons_frame, text="Create", command=self.create_salgrade)
        self.create_salgrade_button.grid(row=0, column=0, pady=5)
        self.read_salgrade_button = tk.Button(self.salgrade_buttons_frame, text="Read", command=self.read_salgrade)
        self.read_salgrade_button.grid(row=0, column=1, pady=5)
        self.update_salgrade_button = tk.Button(self.salgrade_buttons_frame, text="Update", command=self.update_salgrade)
        self.update_salgrade_button.grid(row=0, column=2, pady=5)
        self.delete_salgrade_button = tk.Button(self.salgrade_buttons_frame, text="Delete", command=self.delete_salgrade)
        self.delete_salgrade_button.grid(row=0, column=3, pady=5)
        self.clear_salgrade_button = tk.Button(self.salgrade_buttons_frame, text="Clear", command=self.clear_salgrade_entries)
        self.clear_salgrade_button.grid(row=0, column=4, pady=5)
    def create_employee(self):
        try:
            empno = int(self.empno_entry.get())
            ename = self.ename_entry.get()
            job = self.job_entry.get()
            mgr = int(self.mgr_entry.get()) if self.mgr_entry.get() else None
            hiredate = self.hiredate_entry.get()
            sal = float(self.sal_entry.get())
            comm = float(self.comm_entry.get()) if self.comm_entry.get() else None
            deptno = int(self.deptno_entry.get())
            new_employee = Employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
            self.db_emp.create_employee(new_employee)
            messagebox.showinfo("Success", "Employee created successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")
    def read_employee(self):
        try:
            empno = int(self.empno_entry.get())
            employee = self.db_emp.read_employee(empno)
            if employee:
                self.empno_entry.delete(0, tk.END)
                self.empno_entry.insert(0, employee.empno)
                self.ename_entry.delete(0, tk.END)
                self.ename_entry.insert(0, employee.ename)
                self.job_entry.delete(0, tk.END)
                self.job_entry.insert(0, employee.job)
                self.mgr_entry.delete(0, tk.END)
                self.mgr_entry.insert(0, employee.mgr)
                self.hiredate_entry.delete(0, tk.END)
                self.hiredate_entry.insert(0, employee.hiredate)
                self.sal_entry.delete(0, tk.END)
                self.sal_entry.insert(0, employee.sal)
                self.comm_entry.delete(0, tk.END)
                self.comm_entry.insert(0, employee.comm)
                self.deptno_entry.delete(0, tk.END)
                self.deptno_entry.insert(0, employee.deptno)
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid empno.")
    def update_employee(self):
        try:
            empno = int(self.empno_entry.get())
            ename = self.ename_entry.get()
            job = self.job_entry.get()
            mgr = int(self.mgr_entry.get()) if self.mgr_entry.get() else None
            hiredate = self.hiredate_entry.get()
            sal = float(self.sal_entry.get())
            comm = float(self.comm_entry.get()) if self.comm_entry.get() else None
            deptno = int(self.deptno_entry.get())
            updated_employee = Employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
            self.db_emp.update_employee(updated_employee)
            messagebox.showinfo("Success", "Employee updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")
    def delete_employee(self):
        try:
            empno = int(self.empno_entry.get())
            self.db_emp.delete_employee(empno)
            messagebox.showinfo("Success", "Employee deleted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid empno.")
    def clear_emp_entries(self):
        self.empno_entry.delete(0, tk.END)
        self.ename_entry.delete(0, tk.END)
        self.job_entry.delete(0, tk.END)
        self.mgr_entry.delete(0, tk.END)
        self.hiredate_entry.delete(0, tk.END)
        self.sal_entry.delete(0, tk.END)
        self.comm_entry.delete(0, tk.END)
        self.deptno_entry.delete(0, tk.END)
    def create_salgrade(self):
        try:
            grade = int(self.grade_entry.get())
            losal = float(self.losal_entry.get())
            hisal = float(self.hisal_entry.get())
            new_salgrade = SalGrade(grade, losal, hisal)
            self.db_salgrade.create_salgrade(new_salgrade)
            messagebox.showinfo("Success", "SalGrade created successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")
    def read_salgrade(self):
        try:
            grade = int(self.grade_entry.get())
            salgrade = self.db_salgrade.read_salgrade(grade)
            if salgrade:
                self.grade_entry.delete(0, tk.END)
                self.grade_entry.insert(0, salgrade.grade)
                self.losal_entry.delete(0, tk.END)
                self.losal_entry.insert(0, salgrade.losal)
                self.hisal_entry.delete(0, tk.END)
                self.hisal_entry.insert(0, salgrade.hisal)
            else:
                messagebox.showerror("Error", "SalGrade not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid grade.")
    def update_salgrade(self):
        try:
            grade = int(self.grade_entry.get())
            losal = float(self.losal_entry.get())
            hisal = float(self.hisal_entry.get())
            updated_salgrade = SalGrade(grade, losal, hisal)
            self.db_salgrade.update_salgrade(updated_salgrade)
            messagebox.showinfo("Success", "SalGrade updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")
    def delete_salgrade(self):
        try:
            grade = int(self.grade_entry.get())
            self.db_salgrade.delete_salgrade(grade)
            messagebox.showinfo("Success", "SalGrade deleted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid grade.")
    def clear_salgrade_entries(self):
        self.grade_entry.delete(0, tk.END)
        self.losal_entry.delete(0, tk.END)
        self.hisal_entry.delete(0, tk.END)
def main():
    app = EmpApp('company.db')
    app.mainloop()
    
main()    