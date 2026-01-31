import tkinter as tk
from tkinter import messagebox, ttk
employees = [
    {"empno": 7369, "ename": "WAHID", "job": "CLERK", "mgr": 7902, "hiredate": "1993-06-13", "sal": 8000.00, "comm": None, "deptno": 20},
    {"empno": 7499, "ename": "AHMAD", "job": "SALESMAN", "mgr": 7698, "hiredate": "1998-08-15", "sal": 16000.00, "comm": 300.00, "deptno": 30},

]
class EmpApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Management System")
        self.geometry("800x400")
        self.create_widgets()
    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("empno", "ename", "job", "mgr", "hiredate", "sal", "comm", "deptno"), show="headings")
        self.tree.heading("empno", text="Emp No")
        self.tree.heading("ename", text="Name")
        self.tree.heading("job", text="Job")
        self.tree.heading("mgr", text="Manager")
        self.tree.heading("hiredate", text="Hire Date")
        self.tree.heading("sal", text="Salary")
        self.tree.heading("comm", text="Commission")
        self.tree.heading("deptno", text="Dept No")
        for emp in employees:
            self.tree.insert("", "end", values=(emp["empno"], emp["ename"], emp["job"], emp["mgr"], emp["hiredate"], emp["sal"], emp["comm"], emp["deptno"]))

        self.tree.pack(expand=True, fill=tk.BOTH)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, expand=True)
        
        add_btn = tk.Button(btn_frame, text="Add", command=self.add_employee)
        edit_btn = tk.Button(btn_frame, text="Edit", command=self.edit_employee)
        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_employee)
        
        add_btn.pack(side=tk.LEFT, padx=5, pady=5)
        edit_btn.pack(side=tk.LEFT, padx=5, pady=5)
        delete_btn.pack(side=tk.LEFT, padx=5, pady=5)

    def add_employee(self):
        EmpDetailWindow(self, "Add Employee")

    def edit_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an employee to edit")
            return
        emp_values = self.tree.item(selected_item[0], "values")
        EmpDetailWindow(self, "Edit Employee", emp_values)

    def delete_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an employee to delete")
            return
        emp_values = self.tree.item(selected_item[0], "values")
        self.tree.delete(selected_item[0])
        messagebox.showinfo("Info", f"Employee {emp_values[1]} deleted successfully")

class EmpDetailWindow(tk.Toplevel):
    def __init__(self, parent, title, emp_values=None):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x300")
        self.parent = parent
        self.emp_values = emp_values

        self.create_widgets()

    def create_widgets(self):
        self.empno_var = tk.StringVar(value=self.emp_values[0] if self.emp_values else "")
        self.ename_var = tk.StringVar(value=self.emp_values[1] if self.emp_values else "")
        self.job_var = tk.StringVar(value=self.emp_values[2] if self.emp_values else "")
        self.mgr_var = tk.StringVar(value=self.emp_values[3] if self.emp_values else "")
        self.hiredate_var = tk.StringVar(value=self.emp_values[4] if self.emp_values else "")
        self.sal_var = tk.StringVar(value=self.emp_values[5] if self.emp_values else "")
        self.comm_var = tk.StringVar(value=self.emp_values[6] if self.emp_values else "")
        self.deptno_var = tk.StringVar(value=self.emp_values[7] if self.emp_values else "")

        tk.Label(self, text="Emp No:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.empno_var).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.ename_var).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Job:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.job_var).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Manager:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.mgr_var).grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Hire Date:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.hiredate_var).grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Salary:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.sal_var).grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Commission:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.comm_var).grid(row=6, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Dept No:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.deptno_var).grid(row=7, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=8, columnspan=2, pady=10)

        if self.emp_values:
            update_btn = tk.Button(btn_frame, text="Update", command=self.update_employee)
            update_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        else:
            add_btn = tk.Button(btn_frame, text="Add", command=self.add_employee)
            add_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.destroy)
        cancel_btn.pack(side=tk.LEFT, padx=5, pady=5)
    
    def add_employee(self):
        new_emp = {
            "empno": self.empno_var.get(),
            "ename": self.ename_var.get(),
            "job": self.job_var.get(),
            "mgr": self.mgr_var.get(),
            "hiredate": self.hiredate_var.get(),
            "sal": self.sal_var.get(),
            "comm": self.comm_var.get(),
            "deptno": self.deptno_var.get()
        }
        self.parent.tree.insert("", "end", values=tuple(new_emp.values()))
        messagebox.showinfo("Info", "Employee added successfully")
        self.destroy()
    
    def update_employee(self):
        selected_item = self.parent.tree.selection()[0]
        self.parent.tree.item(selected_item, values=(
            self.empno_var.get(),
            self.ename_var.get(),
            self.job_var.get(),
            self.mgr_var.get(),
            self.hiredate_var.get(),
            self.sal_var.get(),
            self.comm_var.get(),
            self.deptno_var.get()
        ))
        messagebox.showinfo("Info", "Employee updated successfully")
        self.destroy()

def main():
    app = EmpApp()
    app.mainloop()
main()    