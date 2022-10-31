from person import Person
from random import randint
import copy

class Student(Person):

    def __init__(self, person):
        self.person = person
        self.marks = []

    def add_marks(self,mark):
        self.marks.append(mark)

    def add_marks_FP(self,mark):
        marks_cha = copy.deepcopy(self.marks)
        marks_cha.append(mark)
        student_cha = Student(self.person)
        student_cha.marks = marks_cha
        return student_cha

    def average_marks(self):
        sum_marks = sum((int(self.marks[i]) for i in range(0, int(len(self.marks)))))
        return sum_marks / len(self.marks)

    def get_person(self):
        return self.person
    
    def get_marks(self):
        return self.marks
