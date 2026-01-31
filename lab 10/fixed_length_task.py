import os


CODE_LENGTH = 8
TITLE_LENGTH = 40
CREDITS_LENGTH = 3
SEMESTER_LENGTH = 2
TYPE_LENGTH = 8

def display_menu():
    print("Menu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("q) Quit")

def add_course():
    code = input("Enter course code (max 8 characters): ")
    title = input("Enter course title (max 40 characters): ")
    credits = input("Enter credits hours: ")
    semester = input("Enter default semester: ")
    course_type = input("Enter course type (core/elective): ")


    code = code.ljust(CODE_LENGTH)[:CODE_LENGTH]
    title = title.ljust(TITLE_LENGTH)[:TITLE_LENGTH]
    credits = credits.rjust(CREDITS_LENGTH)[:CREDITS_LENGTH]
    semester = semester.rjust(SEMESTER_LENGTH)[:SEMESTER_LENGTH]
    course_type = course_type.ljust(TYPE_LENGTH)[:TYPE_LENGTH]

    with open("courses.txt", "a") as file:
        file.write(f"{code}{title}{credits}{semester}{course_type}\n")
    print("Course added successfully.")

def search_course():
    code_to_search = input("Enter course code to search: ")

    with open("courses.txt", "r") as file:
        for line in file:
            code = line[:CODE_LENGTH].strip()
            if code == code_to_search:
                print(line.strip())
                return
    print("Course not found.")

def delete_course():
    code_to_delete = input("Enter course code to delete: ")

    with open("courses.txt", "r") as file:
        lines = file.readlines()

    with open("courses.txt", "w") as file:
        for line in lines:
            code = line[:CODE_LENGTH].strip()
            if code != code_to_delete:
                file.write(line)
    print("Course deleted successfully.")

def list_all_courses():
    with open("courses.txt", "r") as file:
        for line in file:
            print(line.strip())

def edit_course():
    code_to_edit = input("Enter course code to edit: ")
    new_title = input("Enter new title (max 40 characters): ")
    new_credits = input("Enter new credits hours: ")
    new_semester = input("Enter new default semester: ")
    new_type = input("Enter new course type (core/elective): ")

  
    new_title = new_title.ljust(TITLE_LENGTH)[:TITLE_LENGTH]
    new_credits = new_credits.rjust(CREDITS_LENGTH)[:CREDITS_LENGTH]
    new_semester = new_semester.rjust(SEMESTER_LENGTH)[:SEMESTER_LENGTH]
    new_type = new_type.ljust(TYPE_LENGTH)[:TYPE_LENGTH]

    with open("courses.txt", "r") as file:
        lines = file.readlines()

    with open("courses.txt", "w") as file:
        for line in lines:
            code = line[:CODE_LENGTH].strip()
            if code == code_to_edit:
                line = f"{code}{new_title}{new_credits}{new_semester}{new_type}\n"
            file.write(line)
    print("Course edited successfully.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            add_course()
        elif choice == 's':
            search_course()
        elif choice == 'd':
            delete_course()
        elif choice == 'l':
            list_all_courses()
        elif choice == 'e':
            edit_course()
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please choose from the options below.")

if __name__ == "__main__":
    main()
