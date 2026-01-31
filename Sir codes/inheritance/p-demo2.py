from abc import ABC, abstractproperty

class Student(ABC):
    def __init__(self, n, r, s):
        self.name = n
        self.rollno = r
        self.semester = s
    
    @property
    def Subject(self):
        return "Math"

    @property
    def Name(self):
        return self.name
        
    @property
    def RollNo(self):
        return self.rollno
        
    @property
    def Semester(self):
        return self.semester

    @abstractproperty
    def Marks(self):
        pass

class MathStudent(Student):
    def __init__(self, n, r, s, om, tm):
        super().__init__(n, r, s)
        self.obtained_marks = om
        self.total_marks = tm
    
    @property
    def Marks(self):
        return 100*self.obtained_marks/self.total_marks
        
class EngrStudent(Student):
    def __init__(self, n, r, s, om, tm, pr):
        super().__init__(n, r, s)
        self.obtained_marks = om
        self.total_marks = tm
        self.practicle_marks = pr
            
    @property
    def Marks(self):
        return 70*self.obtained_marks/self.total_marks+self.practicle_marks
        
def main():
    students = []
    students.append(MathStudent('Arshad', 21, 2, 120, 150))
    students.append(EngrStudent('Navaid', 54, 3, 55, 60, 25))
    students.append(EngrStudent('Zaid', 57, 3, 45, 60, 21))
    students.append(MathStudent('Lateef', 76, 5, 42, 70))
    students.append(EngrStudent('Qabil', 51, 3, 52, 60, 27))
    
    for s in students:
        print(s.Subject, end=" ")
        print(s.Name.ljust(8), end=" ")
        print(s.RollNo, end=" ")
        print(s.Semester, end=" ")
        print(round(s.Marks,1), end=" ")
        print()
        
main()     
        

        
        
        