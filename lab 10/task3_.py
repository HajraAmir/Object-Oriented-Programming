import pickle
import os

filename = 'courses_data.pkl'
def load_data():
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return {}

def save_data(courses):
    with open(filename, 'wb') as file:
        pickle.dump(courses, file)


def display_menu():
    menu = (
        "Menu:\n"
        "a) Add\n"
        "s) Search\n"
        "d) Delete\n"
        "l) List All\n"
        "e) Edit\n"
        "q) Quit\n"
        "Choose an option: "
    )
    return input(menu)


def add_course(courses):
    code = input("Enter course code : ")[:8]
    title = input("Enter course title : ")[:40]
    credit_hours = int(input("Enter credit hours: "))
    default_semester = int(input("Enter default semester: "))
    course_type = input("Enter course type (core/elective): ").lower()
    while course_type not in ['core', 'elective']:
        print("Invalid type. Please enter 'core' or 'elective'.")
        course_type = input("Enter course type (core/elective): ").lower()

    courses[code] = {
        'title': title,
        'credit_hours': credit_hours,
        'default_semester': default_semester,
        'type': course_type
    }
    save_data(courses)
    print("Course added successfully.")


def search_course(courses):
    code = input("Enter course code to search: ")
    if code in courses:
        course = courses[code]
        print("Course Found:")
        print(f"Code: {code}, Title: {course['title']}, Credits: {course['credit_hours']}, Semester: {course['default_semester']}, Type: {course['type']}")
    else:
        print("Course not found.")


def delete_course(courses):
    code = input("Enter course code to delete: ")
    if code in courses:
        del courses[code]
        save_data(courses)
        print("Course deleted successfully.")
    else:
        print("Course not found.")

def list_courses(courses):
    if courses:
        print("Listing all courses:")
        for code, course in courses.items():
            print(f"Code: {code}, Title: {course['title']}, Credits: {course['credit_hours']}, Semester: {course['default_semester']}, Type: {course['type']}")
    else:
        print("No courses available.")


def edit_course(courses):
    code = input("Enter course code to edit: ")
    if code in courses:
        print("Enter new details (leave blank to keep current):")
        title = input("New title: ") or courses[code]['title']
        credit_hours = input("New credit hours: ")
        credit_hours = int(credit_hours) if credit_hours else courses[code]['credit_hours']
        default_semester = input("New default semester: ")
        default_semester = int(default_semester) if default_semester else courses[code]['default_semester']
        course_type = input("New type (core/elective): ") or courses[code]['type']

        courses[code] = {
            'title': title,
            'credit_hours': credit_hours,
            'default_semester': default_semester,
            'type': course_type
        }
        save_data(courses)
        print("Course updated successfully.")
    else:
        print("Course not found.")


def main():
    courses = load_data()
    
    while True:
        option = display_menu()
        if option == 'a':
            add_course(courses)
        elif option == 's':
            search_course(courses)
        elif option == 'd':
            delete_course(courses)
        elif option == 'l':
            list_courses(courses)
        elif option == 'e':
            edit_course(courses)
        elif option == 'q':
            print("Quitting program.")
            break
        else:
            print("Invalid input, choose from below mentioned options.")


main()