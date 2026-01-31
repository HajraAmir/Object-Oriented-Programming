import tkinter as tk
from tkinter import messagebox
import sqlite3

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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS SALGRADE (
                GRADE INTEGER PRIMARY KEY,
                LOSAL REAL,
                HISAL REAL
            )
        ''')
        self.conn.commit()

    def create_salgrade(self, salgrade):
        self.cursor.execute("INSERT INTO SALGRADE (GRADE, LOSAL, HISAL) VALUES (?, ?, ?)",
                            (salgrade.grade, salgrade.losal, salgrade.hisal))
        self.conn.commit()

    def read_salgrade(self, grade):
        self.cursor.execute("SELECT * FROM SALGRADE WHERE GRADE=?", (grade,))
        row = self.cursor.fetchone()
        if row:
            return SalGrade(row[0], row[1], row[2])
        else:
            return None

    def update_salgrade(self, salgrade):
        self.cursor.execute("UPDATE SALGRADE SET LOSAL=?, HISAL=? WHERE GRADE=?",
                            (salgrade.losal, salgrade.hisal, salgrade.grade))
        self.conn.commit()

    def delete_salgrade(self, grade):
        self.cursor.execute("DELETE FROM SALGRADE WHERE GRADE=?", (grade,))
        self.conn.commit()

class Application(tk.Tk):
    def __init__(self, db_file):
        super().__init__()
        self.title("SalGrade Management")
        self.db = SalGradeDB(db_file)

        self.create_widgets()

    def create_widgets(self):
        self.data_frame = tk.Frame(self)
        self.data_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        tk.Label(self.data_frame, text="Grade:").grid(row=0, column=0)
        tk.Label(self.data_frame, text="Lowest Salary:").grid(row=1, column=0)
        tk.Label(self.data_frame, text="Highest Salary:").grid(row=2, column=0)

        self.grade_entry = tk.Entry(self.data_frame)
        self.grade_entry.grid(row=0, column=1)
        self.losal_entry = tk.Entry(self.data_frame)
        self.losal_entry.grid(row=1, column=1)
        self.hisal_entry = tk.Entry(self.data_frame)
        self.hisal_entry.grid(row=2, column=1)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        
        self.create_button = tk.Button(self.buttons_frame, text="Create", command=self.create_grade)
        self.create_button.grid(row=0, column=0, pady=5)
        self.read_button = tk.Button(self.buttons_frame, text="Read", command=self.read_grade)
        self.read_button.grid(row=0, column=1, pady=5)
        self.update_button = tk.Button(self.buttons_frame, text="Update", command=self.update_grade)
        self.update_button.grid(row=0, column=2, pady=5)
        self.delete_button = tk.Button(self.buttons_frame, text="Delete", command=self.delete_grade)
        self.delete_button.grid(row=0, column=3, pady=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", command=self.clear_grade)
        self.clear_button.grid(row=0, column=4, pady=5)
        self.show_button = tk.Button(self.buttons_frame, text="Show", command=self.show_grade_window)
        self.show_button.grid(row=0, column=5, pady=5)

    def create_grade(self):
        try:
            grade = int(self.grade_entry.get())
            losal = float(self.losal_entry.get())
            hisal = float(self.hisal_entry.get())
            new_grade = SalGrade(grade, losal, hisal)
            self.db.create_salgrade(new_grade)
            messagebox.showinfo("Success", "Grade {} created successfully.".format(grade))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def read_grade(self):
        try:
            grade = int(self.grade_entry.get())
            salgrade = self.db.read_salgrade(grade)
            if salgrade:
                self.grade_entry.delete('0', 'end')
                self.losal_entry.delete('0', 'end')
                self.hisal_entry.delete('0', 'end')
                self.grade_entry.insert('0', str(salgrade.grade))
                self.losal_entry.insert('0', str(salgrade.losal))
                self.hisal_entry.insert('0', str(salgrade.hisal))
            else:
                messagebox.showerror("Error", "Grade {} not found.".format(grade))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid grade.")

    def update_grade(self):
        try:
            grade = int(self.grade_entry.get())
            losal = float(self.losal_entry.get())
            hisal = float(self.hisal_entry.get())
            updated_grade = SalGrade(grade, losal, hisal)
            self.db.update_salgrade(updated_grade)
            messagebox.showinfo("Success", "Grade {} updated successfully.".format(grade))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def delete_grade(self):
        try:
            grade = int(self.grade_entry.get())
            self.db.delete_salgrade(grade)
            messagebox.showinfo("Success", "Grade {} deleted successfully.".format(grade))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid grade.")

    def clear_grade(self):
        self.grade_entry.delete('0', 'end')
        self.losal_entry.delete('0', 'end')
        self.hisal_entry.delete('0', 'end')

    def show_grade_window(self):
        try:
            grade = int(self.grade_entry.get())
            salgrade = self.db.read_salgrade(grade)
            if (salgrade):
                show_window = tk.Toplevel(self)
                show_window.title(f"Grade {grade} Details")

                tk.Label(show_window, text="Grade:").grid(row=0, column=0)
                tk.Label(show_window, text="Lowest Salary:").grid(row=1, column=0)
                tk.Label(show_window, text="Highest Salary:").grid(row=2, column=0)

                grade_label = tk.Label(show_window, text=str(salgrade.grade))
                grade_label.grid(row=0, column=1)
                losal_label = tk.Label(show_window, text=str(salgrade.losal))
                losal_label.grid(row=1, column=1)
                hisal_label = tk.Label(show_window, text=str(salgrade.hisal))
                hisal_label.grid(row=2, column=1)
            else:
                messagebox.showerror("Error", "Grade {} not found.".format(grade))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid grade.")

def main():
    app = Application('salgrade.db')
    app.mainloop()
main()    