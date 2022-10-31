from universityclass import UniversityClass
from teacher import Teacher


class Lesson(UniversityClass, Teacher):

    def __init__(self, number_classroom, teacher, university_class):
        self.number_classroom = number_classroom
        self.teacher = teacher
        self.university_class = university_class