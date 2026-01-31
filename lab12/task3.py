import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("your_database.db")
cursor = conn.cursor()

def add_grade():
    grade = int(grade_entry.get())
    losal = float(losal_entry.get())
    hisal = float(hisal_entry.get())
    try:
        cursor.execute("INSERT INTO salgrade (grade, losal, hisal) VALUES (?, ?, ?)", (grade, losal, hisal))
        conn.commit()
        messagebox.showinfo("Success", "Grade added successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to add grade: {e}")

def search_grade():
    grade = int(grade_search_entry.get())
    cursor.execute("SELECT * FROM salgrade WHERE grade = ?", (grade,))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Grade Found", f"Grade: {result}")
    else:
        messagebox.showinfo("Grade Not Found", "Grade not found.")

def update_grade():
    grade = int(grade_update_entry.get())
    losal = float(losal_update_entry.get())
    hisal = float(hisal_update_entry.get())
    try:
        cursor.execute("UPDATE salgrade SET losal = ?, hisal = ? WHERE grade = ?", (losal, hisal, grade))
        conn.commit()
        messagebox.showinfo("Success", "Grade updated successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to update grade: {e}")

def delete_grade():
    grade = int(grade_delete_entry.get())
    try:
        cursor.execute("DELETE FROM salgrade WHERE grade = ?", (grade,))
        conn.commit()
        messagebox.showinfo("Success", "Grade deleted successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to delete grade: {e}")

def list_all_grades():
    cursor.execute("SELECT * FROM salgrade")
    result = cursor.fetchall()
    if result:
        messagebox.showinfo("All Grades", "\n".join(str(row) for row in result))
    else:
        messagebox.showinfo("No Grades Found", "No grades found.")
root = tk.Tk()
root.title("Grade Management System")
add_frame = tk.Frame(root)
add_frame.pack(pady=10)
tk.Label(add_frame, text="Grade Number:").grid(row=0, column=0)
grade_entry = tk.Entry(add_frame)
grade_entry.grid(row=0, column=1)
tk.Label(add_frame, text="Lowest Salary:").grid(row=1, column=0)
losal_entry = tk.Entry(add_frame)
losal_entry.grid(row=1, column=1)
tk.Label(add_frame, text="Highest Salary:").grid(row=2, column=0)
hisal_entry = tk.Entry(add_frame)
hisal_entry.grid(row=2, column=1)
add_button = tk.Button(add_frame, text="Add Grade", command=add_grade)
add_button.grid(row=3, columnspan=2)
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
tk.Label(search_frame, text="Grade Number to Search:").grid(row=0, column=0)
grade_search_entry = tk.Entry(search_frame)
grade_search_entry.grid(row=0, column=1)
search_button = tk.Button(search_frame, text="Search Grade", command=search_grade)
search_button.grid(row=1, columnspan=2)
update_frame = tk.Frame(root)
update_frame.pack(pady=10)
tk.Label(update_frame, text="Grade Number to Update:").grid(row=0, column=0)
grade_update_entry = tk.Entry(update_frame)
grade_update_entry.grid(row=0, column=1)
tk.Label(update_frame, text="New Lowest Salary:").grid(row=1, column=0)
losal_update_entry = tk.Entry(update_frame)
losal_update_entry.grid(row=1, column=1)
tk.Label(update_frame, text="New Highest Salary:").grid(row=2, column=0)
hisal_update_entry = tk.Entry(update_frame)
hisal_update_entry.grid(row=2, column=1)
update_button = tk.Button(update_frame, text="Update Grade", command=update_grade)
update_button.grid(row=3, columnspan=2)
delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)
tk.Label(delete_frame, text="Grade Number to Delete:").grid(row=0, column=0)
grade_delete_entry = tk.Entry(delete_frame)
grade_delete_entry.grid(row=0, column=1)
delete_button = tk.Button(delete_frame, text="Delete Grade", command=delete_grade)
delete_button.grid(row=1, columnspan=2)
list_button = tk.Button(root, text="List All Grades", command=list_all_grades)
list_button.pack(pady=10)
root.mainloop()
cursor.close()
conn.close()