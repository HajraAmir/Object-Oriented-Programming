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
sub1=Subject("DSA101", "DSA", 4)
sub2=Subject("DATA201", "Database", 4)
sub3=Subject("CAL101", "Calculus", 3)
sub4=Subject("LIN101", "Linear", 3)
enrolled_sub1=EnrolledSubject(sub1, 85)
enrolled_sub2=EnrolledSubject(sub2, 78)
enrolled_sub3=EnrolledSubject(sub3, 92)
enrolled_sub4=EnrolledSubject(sub4, 80)
stud1=Student("001", "HAJRA", 2, [enrolled_sub1, enrolled_sub2, enrolled_sub3, enrolled_sub4])
stud2=Student("002", "RABIA", 3, [enrolled_sub2, enrolled_sub3, enrolled_sub4, enrolled_sub1])
stud3=Student("003", "MANO", 1, [enrolled_sub3, enrolled_sub4, enrolled_sub1, enrolled_sub2])
stud4=Student("004", "SIDRA", 4, [enrolled_sub4, enrolled_sub1, enrolled_sub2, enrolled_sub3])
students=[stud1, stud2, stud3, stud4]
with open('studs.pkl', 'wb') as file:
    for student in students:
        pickle.dump(student, file)
with open('studs.pkl', 'rb') as file:
    while True:
        try:
            student = pickle.load(file)
            print("Roll No:", student.rollno)
            print("Name:", student.name)
            print("Semester:", student.semester)
            print("Enrolled Subjects:")
            for enrolled_subject in student.enrolled_subjects:
                print("  Code:", enrolled_subject.subject.code)
                print("  Name:", enrolled_subject.subject.name)
                print("  Credits:", enrolled_subject.subject.credits)
                print("  Percent Marks:", enrolled_subject.percent_marks)
            print()
        except EOFError:
            break