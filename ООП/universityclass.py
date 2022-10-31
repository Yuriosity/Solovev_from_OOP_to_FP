from student import Student
from teacher import Teacher


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