import pickle

class Subject:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits

class EnrolledSubject:
    def __init__(self, subject, percent_marks):
        self.subject = subject
        self.percent_marks = percent_marks

class Student:
    def __init__(self, rollno, name, semester, enrolled_subjects):
        self.rollno = rollno
        self.name = name
        self.semester = semester
        self.enrolled_subjects = enrolled_subjects


subjects = [
    Subject("001", "Mathematics", 3),
    Subject("002", "Science", 4),
    Subject("003", "History", 2),
    Subject("004", "English", 3)
]


enrolled_subjects_1 = [
    EnrolledSubject(subjects[0], 85),
    EnrolledSubject(subjects[1], 78),
    EnrolledSubject(subjects[2], 92),
    EnrolledSubject(subjects[3], 88)
]


students = [
    Student("1", "John Doe", 2, enrolled_subjects_1),
    Student("2", "Jane Smith", 3, enrolled_subjects_1),
    Student("3", "Alice Johnson", 1, enrolled_subjects_1),
    Student("4", "Bob Brown", 4, enrolled_subjects_1)
]


with open('studs.pkl', 'wb') as file:
    for student in students:
        pickle.dump(student, file)

print("Student records saved successfully.")