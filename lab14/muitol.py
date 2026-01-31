class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
    def __str__(self) :
        return f'Name: {self.name}\nContact: {self.contact}'

class Student(Person):
    def __init__(self, name, contact, department='', semester=None):
        super().__init__(name, contact)
        self.department = department
        self.semester = semester
    def _str_(self) :
        return f'Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}'

class Teacher(Person):
    def __init__(self, name, contact, course, office_number):
        super().__init__(name, contact)
        self.course = course
        self.office_number = office_number
    def __str__(self) :
        return f'Name: {self.name}\nContact: {self.contact}\nCourse: {self.course}\nOffice no.: {self.office_number}'

class TA(Teacher, Student):
    def __init__(self, name, contact, department, semester, course, office_number):
        Teacher.__init__(self, name=name, contact=contact, course=course, office_number=office_number)
        Student.__init__(self, name=name, contact=contact, department=department, semester=semester)
    def __str__(self):
        return f"\nName: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\n" \
               f"Semester: {self.semester}\nCourse: {self.course}\nOffice Number: {self.office_number}"

def main():
    prsn = Person("kashaf", "1234567890")
    student = Student("tehreem", "9567890988", "DS", 2)
    teacher = Teacher("muhammad idrees", "5551234567", "DS", "CSC101")
    ta = TA("ali", "123450876", "DS", 2, "DSC201", "Office123")
    print("Person:")
    print(prsn)
    print("\nStudent:")
    print(student)
    print("\nTeacher:")
    print(teacher)
    print("\nTeaching Assistant:")
    print(ta)
main()