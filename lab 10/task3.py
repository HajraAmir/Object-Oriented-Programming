import pickle

# Define the Course class
class Course:
    def __init__(self, code, title, credit_hours, default_semester, course_type):
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        self.default_semester = default_semester
        self.course_type = course_type

    def __repr__(self):
        return (f"Course(code='{self.code}', title='{self.title}', credit_hours={self.credit_hours}, "
                f"default_semester={self.default_semester}, course_type='{self.course_type}')")

# File name to store the courses data
FILENAME = 'courses.pkl'

# Helper functions to save and load courses data
def save_courses(courses):
    with open(FILENAME, 'wb') as file:
        pickle.dump(courses, file)

def load_courses():
    try:
        with open(FILENAME, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Function to add a new course
def add_course(courses):
    code = input("Enter course code (max 8 characters): ").strip()[:8]
    title = input("Enter course title (max 40 characters): ").strip()[:40]
    credit_hours = int(input("Enter credit hours: "))
    default_semester = int(input("Enter default semester: "))
    course_type = input("Enter course type (core/elective): ").strip()
    
    new_course = Course(code, title, credit_hours, default_semester, course_type)
    courses.append(new_course)
    save_courses(courses)
    print(f"Course {code} added successfully.")

# Function to search for a course by code
def search_course(courses):
    code = input("Enter course code to search: ").strip()
    for course in courses:
        if course.code == code:
            print(course)
            return
    print(f"No course found with code {code}.")

# Function to delete a course by code
def delete_course(courses):
    code = input("Enter course code to delete: ").strip()
    for course in courses:
        if course.code == code:
            courses.remove(course)
            save_courses(courses)
            print(f"Course {code} deleted successfully.")
            return
    print(f"No course found with code {code}.")

# Function to list all courses
def list_courses(courses):
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(course)

# Function to edit a course by code
def edit_course(courses):
    code = input("Enter course code to edit: ").strip()
    for course in courses:
        if course.code == code:
            print(f"Editing course: {course}")
            course.title = input(f"Enter new title (current: {course.title}): ").strip()[:40] or course.title
            course.credit_hours = int(input(f"Enter new credit hours (current: {course.credit_hours}): ") or course.credit_hours)
            course.default_semester = int(input(f"Enter new default semester (current: {course.default_semester}): ") or course.default_semester)
            course.course_type = input(f"Enter new course type (current: {course.course_type}): ").strip() or course.course_type
            save_courses(courses)
            print(f"Course {code} updated successfully.")
            return
    print(f"No course found with code {code}.")

# Main function to display menu and handle user input
def main():
    courses = load_courses()
    menu = """
    Choose an option:
    a) Add
    s) Search
    d) Delete
    l) List All
    e) Edit
    q) Quit
    """
    
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'a':
            add_course(courses)
        elif choice == 's':
            search_course(courses)
        elif choice == 'd':
            delete_course(courses)
        elif choice == 'l':
            list_courses(courses)
        elif choice == 'e':
            edit_course(courses)
        elif choice == 'q':
            print("Quitting program.")
            break
        else:
            print("Invalid input, please choose from the options below.")

# Run the program
if __name__ == "__main__":
    main()
