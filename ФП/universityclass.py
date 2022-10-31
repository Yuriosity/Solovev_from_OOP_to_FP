from student import Student
from teacher import Teacher
import copy

class UniversityClass(Student, Teacher):

    def __init__(self, number):
        self.number = number
        self.students = []
    
    def get_number(self):
        return self.number
    
    def get_students(self):
        return self.students
    
    def add_student(self, student):
        return self.students.append(student)

    def add_student_FP(self, student):
        students_cha = copy.deepcopy(self.students)
        students_cha.append(student)
        universityclass_cha = UniversityClass(self.number)
        universityclass_cha.marks = students_cha
        return universityclass_cha