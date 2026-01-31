import pickle

def display_menu():
    print("Menu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("q) Quit")
def add_course(courses):
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    credits_hours = int(input("Enter credits hours: "))
    semester = int(input("Enter default semester: "))
    course_type = input("Enter course type (core/elective): ")

    courses[code] = {
        'title': title,
        'credits_hours': credits_hours,
        'semester': semester,
        'type': course_type
    }
    print("Course added successfully.")

def search_course(courses):
    code = input("Enter course code to search: ")
    if code in courses:
        print("Course found:")
        print(courses[code])
    else:
        print("Course not found.")
def delete_course(courses):
    code = input("Enter course code to delete: ")
    if code in courses:
        del courses[code]
        print("Course deleted successfully.")
    else:
        print("Course not found.")
def list_all_courses(courses):
    print("All courses:")
    for code, details in courses.items():
        print(code + ":", details)

def edit_course(courses):
    code = input("Enter course code to edit: ")
    if code in courses:
        print("Current details:")
        print(courses[code])
        title = input("Enter new course title (leave empty to keep current): ")
        if title:
            courses[code]['title'] = title
        credits_hours = input("Enter new credits hours (leave empty to keep current): ")
        if credits_hours:
            courses[code]['credits_hours'] = int(credits_hours)
        semester = input("Enter new default semester (leave empty to keep current): ")
        if semester:
            courses[code]['semester'] = int(semester)
        course_type = input("Enter new course type (core/elective) (leave empty to keep current): ")
        if course_type:
            courses[code]['type'] = course_type
        print("Course edited successfully.")
    else:
        print("Course not found.")


def main():
    try:
     
        with open("courses.pkl", "r") as file:
            courses = pickle.load(file)
    except FileNotFoundError:
        courses = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            add_course(courses)
        elif choice == 's':
            search_course(courses)
        elif choice == 'd':
            delete_course(courses)
        elif choice == 'l':
            list_all_courses(courses)
        elif choice == 'e':
            edit_course(courses)
        elif choice == 'q':
        
            with open("courses.pkl", "w") as file:
                pickle.dump(courses, file)
            print("Exiting program.")
            break
        else:
            print("Invalid input. Choose from below mentioned options.")


main()