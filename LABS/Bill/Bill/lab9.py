from datetime import date

class Student:
    def __init__(self, name, rollno, department, semester):
        self.name = name
        self.rollno = rollno
        self.department = department
        self.semester = semester

class Course:
    def __init__(self, code, title, credits, percent_marks):
        self.code = code
        self.title = title
        self.credits = credits
        self.percent_marks = percent_marks

class Transcript:
    def __init__(self, student, courses):
        self.student = student
        self.courses = courses
        self.date_issued = date.today()

    def generate_transcript(self):
        print("Transcript")
        print("Date of Issue:", self.date_issued)
        print("Name:", self.student.name)
        print("Roll No:", self.student.rollno)
        print("Department:", self.student.department)
        print("Semester:", self.student.semester)
        print("\nCourse Code\tCourse Title\t\t\t\tCredits\t\tPercentage Marks")

        total_credits = 0
        total_marks = 0

        for course in self.courses:
            print(f"{course.code}\t\t{course.title}\t\t{course.credits}\t\t{course.percent_marks}")
            total_credits += course.credits
            total_marks += course.percent_marks * course.credits

        total_percentage_marks = total_marks / total_credits
        print("\n\t\t\t\t\t\t\tTotal Percentage Marks:", total_percentage_marks)

def main():
    student = Student("John Doe", "2023001", "Computer Science", "2nd semester")
    courses = [
        Course("CS101", "Introduction Computer Science", 2, 9.25),
        Course("CS102", "Data Structures and Algorithms"  , 2, 14.00),
        Course("CS103", "Database Management Systems"     , 2, 7.50),
        Course("CS104", "Programming Fundamentals  "      , 2, 10.47),
        Course("CS105", "Analysis of Algorithms    "          , 4, 5.75),
        Course("CS106", "Advanced Python Programming"     , 2, 5.00)
    ]
    transcript = Transcript(student, courses)
    transcript.generate_transcript()


main()