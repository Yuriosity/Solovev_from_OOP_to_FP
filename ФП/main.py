from distutils.command.sdist import sdist
from pyparsing import empty
from traitlets import default
from lesson import Lesson
from person import Person
from universityclass import UniversityClass
from student import Student
from teacher import Teacher
import copy
from random import randint, randrange
import random
import string

# region generator
 

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_teachers(quantity):
    teachers = []
    i = 0
    while i < quantity:
        random_age = randint(18,80)
        random_name = generate_random_string(randint(5,10))
        random_subject =  generate_random_string(randint(1,3))
        teachers.append(Teacher(Person(random_name, random_age), random_subject))
        i+=1
    return teachers

def generate_students(quantity):
    students = []
    i = 0
    while i < quantity:
        random_age = randint(18,80)
        random_name = generate_random_string(randint(5,10))
        students.append(Student(Person(random_name, random_age)))
        i+=1
    return students
# endregion 

# region Appeals with Inputs

def input_generate():
    print("Здравствуйте, хотите создать случайно сгенерированные данные? Если да, введите <<1>>, если нет, введите <<2>>.")
    return int(input())

def input_quantity(after):
    print("Введите количество" + after + ".")
    try:
        quantity = int(input())
    except:
        print("Неверный ввод. Устанавливается значение 0.")
        quantity = 0
    return quantity

def input_name():
    print("Введите имя.")
    return input()

def input_age():
    print("Введите возраст.")
    try:
        age = int(input())
    except:
        print("Неверный ввод. Устанавливается значение 0.")
        age = 0
    return age

def input_subject():
    print("Введите предмет.")
    return input()

def input_number(before, after):
    print("Введите" + before + "номер" + after + ".")
    try:
        number = int(input())
    except:
        print("Неверный ввод. Устанавливается значение 0.")
        number = 0
    return number

def input_mark():
    print("Введите оценку.")
    try:
        mark = int(input())
    except:
        print("Неверный ввод. Устанавливается значение 0.")
        mark = 0
    return mark

# endregion 

# region all_{}
def all_name(objects):
    objs_name = []
    for i in range(0,len(objects)):
        objs_name.append(f"{i+1}) {objects[i].get_person().get_name()}")
    return objs_name

def all_groups_number(groups):
    groups_number = []
    for i in range(0,len(groups)):
        groups_number.append(f"{i+1}) {groups[i].get_number()}")
    return groups_number

def all_stud_marks(st_num, students):
    stud_mark = []
    for i in range(0,len(students[st_num].get_marks())):
        stud_mark.append(f"{i+1}) {students[st_num].get_marks()[i]}")
    return stud_mark

def all_in_group_name(objects, gr_num, groups):
    objs_name = []
    j = 0
    for i in range(0,len(objects)):
        if(i in groups[gr_num].get_students()):
            j += 1
            objs_name.append(f"{j}) {objects[i].get_person().get_name()}")
    return objs_name
# endregion
 
# region add_{}
def add_student(name, age, students):
    students_cha = copy.deepcopy(students)
    students_cha.append(Student(Person(name, age)))
    return students_cha

def add_teacher(name, age, subject, teachers):
    teachers_cha = copy.deepcopy(teachers)
    teachers_cha.append(Teacher(Person(name, age),subject))
    return teachers_cha

def add_group(gr_num, groups):
    groups_cha = copy.deepcopy(groups)
    groups_cha.append(UniversityClass(gr_num))
    return groups_cha

def add_student_in_groups(gr_num, st_num, groups):
    groups_cha = copy.deepcopy(groups)
    groups_cha[gr_num].add_student(st_num)
    return groups_cha

def add_lesson(teach_num, group_num, clarom_num, teachers, groups, lessons):
    lessons_cha = copy.deepcopy(lessons)
    lessons_cha.append(Lesson(clarom_num, teach_num, group_num))
    return lessons_cha

def add_mark_in_student(st_num, mark, students):
    student_cha = copy.deepcopy(students)
    student_cha[st_num] = student_cha[st_num].add_marks_FP(mark)
    return student_cha
# endregion

def function_list():
    return(
    "---------------------------------------------------\n"+
    "Что хотите сделать?\n"+
    "0) Выйти из программы.\n"+
    "1) Вывести список имен всех студентов.\n"+
    "2) Вывести список имен всех преподавателей.\n"+
    "3) Добавить студента.\n"+
    "4) Добавить преподавателя.\n"+
    "5) Вывести список групп.\n"+
    "6) Создать новую группу.\n"+
    "7) Добавить студента в группу.\n"+
    "8) Назначить занятие.\n"+
    "9) Добавить оценку студенту.\n"+
    "10) Посмотреть оценки студента.\n"+
    "11) Вывести список имен студентов в выбранной группе.\n"+
    "---------------------------------------------------")

def choise_generate(num):
    if num == 1:
        return("Готовимся генерировать!")
    elif num == 2:
        return("Не генерирую!")
    else:
        return("Не генерирую, делайте выбор аккуратнее!")

def normal_output(object):
    if len(object) <= 0:
        print("Здесь еще ничего нет.") 
    for i in range(0,len(object)):
        print(object[i])

def main():
    print(choise_generate(input_generate()))
    teachers = generate_teachers(input_quantity(" учителей"))
    students = generate_students(input_quantity(" студентов"))
    groups = []
    lessons = []
    while True:
        print(function_list())
        match int(input()):
            case 0: 
                print("До свидания!")
                break
            case 1:
                print("Имена всех студентов:")
                normal_output(all_name(students))
            case 2: 
                print("Имена всех преподавателей:")
                normal_output(all_name(teachers))
            case 3: 
                students = add_student(input_name(), input_age(), students)
            case 4: 
                teachers = add_teacher(input_name(), input_age(), input_subject(), teachers)
            case 5:
                print("Номера всех групп:")
                normal_output(all_groups_number(groups))
            case 6: 
                groups = add_group(input_number(" ", " группы"), groups)
            case 7: 
                print("Номера всех групп:")
                normal_output(all_groups_number(groups))
                if len(groups) > 0:
                    gr_num = input_number(" порядковый ", " группы") - 1
                    print("Имена всех студентов:")
                    normal_output(all_name(students))
                    if len(students) > 0: 
                        st_num = input_number(" порядковый ", " cтудента") - 1
                        groups = add_student_in_groups(gr_num, st_num, groups)
            case 8: 
                print("Имена всех преподавателей:")
                normal_output(all_name(teachers))
                if len(teachers) > 0:
                    teach_num = input_number(" порядковый ", " преподавателя") - 1
                    print("Номера всех групп:")
                    normal_output(all_groups_number(groups))
                    if len(groups) > 0:
                        gr_num = input_number(" порядковый ", " группы") - 1
                        clsrom_num = input_number(" ", " кабинета")
                        lessons = add_lesson(teach_num, gr_num, clsrom_num, teachers, groups, lessons)
            case 9: 
                print("Имена всех студентов:")
                normal_output(all_name(students))
                if len(students) > 0:
                    st_num = input_number(" порядковый ", " cтудента") - 1
                    mark = input_mark()
                    students = add_mark_in_student(st_num, mark, students)
            case 10: 
                print("Имена всех студентов:")
                normal_output(all_name(students))
                if len(students) > 0:
                    st_num = input_number(" порядковый ", " cтудента") - 1
                    normal_output(all_stud_marks(st_num, students))
            case 11:
                print("Номера всех групп:")
                normal_output(all_groups_number(groups))
                if len(groups) > 0:
                    gr_num = input_number(" порядковый ", " группы") - 1
                    print("Имена студентов из заданной группы:")
                    normal_output(all_in_group_name(students, gr_num, groups))
            case _: 
                print("Неизвестная команда!")
    return 0

if __name__ == '__main__':
    main()
