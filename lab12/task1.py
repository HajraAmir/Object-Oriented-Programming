import sqlite3


conn = sqlite3.connect('departments.db')
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS dept (
               deptno INTEGER PRIMARY KEY,
               dname TEXT,
               location TEXT)''')


def menu():
    print("Menu:")
    print("a) Add")
    print("s) Search name")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("n) Edit name")
    print("l) Edit location")
    print("q) Quit")


def add_department(deptno, dname, location):
    cur.execute("INSERT INTO dept (deptno, dname, location) VALUES (?, ?, ?)", (deptno, dname, location))
    conn.commit()

def search_department_by_name(dname):
    cur.execute("SELECT * FROM dept WHERE dname=?", (dname,))
    result = cur.fetchall()
    return result


def delete_department(deptno):
    cur.execute("DELETE FROM dept WHERE deptno=?", (deptno,))
    conn.commit()

def list_all_departments():
    cur.execute("SELECT * FROM dept")
    result = cur.fetchall()
    return result

def edit_department(deptno, dname, location):
    cur.execute("UPDATE dept SET dname=?, location=? WHERE deptno=?", (dname, location, deptno))
    conn.commit()


def edit_department_name(deptno, dname):
    cur.execute("UPDATE dept SET dname=? WHERE deptno=?", (dname, deptno))
    conn.commit()


def edit_department_location(deptno, location):
    cur.execute("UPDATE dept SET location=? WHERE deptno=?", (location, deptno))
    conn.commit()


def main():
    while True:
        menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            break
        elif choice == 'a':
            deptno = int(input("Enter department number: "))
            dname = input("Enter department name: ")
            location = input("Enter department location: ")
            add_department(deptno, dname, location)
            print("Department added successfully.")
        elif choice == 's':
            dname = input("Enter department name to search: ")
            result = search_department_by_name(dname)
            if result:
                print("Department found:", result)
            else:
                print("Department not found.")
        elif choice == 'd':
            deptno = int(input("Enter department number to delete: "))
            delete_department(deptno)
            print("Department deleted successfully.")
        elif choice == 'l':
            result = list_all_departments()
            if result:
                for row in result:
                    print(row)
            else:
                print("No departments found.")
        elif choice == 'e':
            deptno = int(input("Enter department number to edit: "))
            dname = input("Enter new department name: ")
            location = input("Enter new department location: ")
            edit_department(deptno, dname, location)
            print("Department edited successfully.")
        elif choice == 'n':
            deptno = int(input("Enter department number to edit name: "))
            dname = input("Enter new department name: ")
            edit_department_name(deptno, dname)
            print("Department name edited successfully.")
        elif choice == 'l':
            deptno = int(input("Enter department number to edit location: "))
            location = input("Enter new department location: ")
            edit_department_location(deptno, location)
            print("Department location edited successfully.")
        else:
            print("Invalid choice. Please try again.")

    conn.close()


main()