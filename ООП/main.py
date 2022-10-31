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

def hello():
    print("Здравствуйте, хотите загрузить случайно сгенерированные данные? Если да, введите <<1>>, если нет, введите <<2>>.")

    choise = int(input())

    if choise == 1:
        print("Загружаю!")
    elif choise == 2:
        print("Не загружаю!")
    else:
        print("Не загружаю, делайте выбор аккуратнее!")

    if(choise == 1):
        persons = []
        f = open('generator.txt')
        person_file = [line.strip() for line in f]
        for i in range(0, len(person_file)):
            persons.append([x.strip() for x in person_file[i].split(';')])
        f.close()

        rand_num_10 = []
        i = 0    
        while i < 10:
            rand_num = randint(1,29)
            rand_num_10.append(rand_num)
            i+=1

        teachers = []
        students = []
        i = 0    
        while i < 30:
            if i in rand_num_10:
                teachers.append(Teacher(Person(persons[i][0], persons[i][1]), persons[i][2]))
            else:
                students.append(Student(Person(persons[i][0], persons[i][1])))
            i+=1
    return persons.copy(),teachers.copy(),students.copy()

def all_stud_name(students):
    studs_name = []
    for i in range(0,len(students)):
        studs_name.append(students[i].get_person().get_name())
    return studs_name

def all_teach_name(teachers):
    teachs_name = []
    for i in range(0,len(teachers)):
        # teachs_name.append(teachers[i].get_person().get_name())
        teachs_name.append(f"{i+1}), {teachers[i].get_person().get_name()}\n")
    return print(teachs_name)

def normal_output(num, object):
    if (num == 1):
        print("Имена студентов: ")
    elif (num == 2):
        print("Имена преподавателей: ")
    if (num == 1) or (num == 2):
        for i in range(0,len(object)):
            print(f"{i+1}) {object[i]}")
    else: print("Такого не бывает!")

def add_student(students):
    print("Введите имя студента.")
    st_name = input()
    print("Введите возраст студента.")
    st_age = int(input())
    new_st = Student(Person(st_name, st_age))
    students_cha = students.copy()
    students_cha.append(new_st)
    return students_cha

def add_teacher(teachers):
    print("Введите имя преподавателя.")
    tc_name = input()
    print("Введите возраст преподавателя.")
    tc_age = int(input())
    print("Введите предмет преподавателя.")
    tc_sub = input()
    new_tc = Teacher(Person(tc_name, tc_age),tc_sub)
    teachers_cha = teachers.copy()
    teachers_cha.append(new_tc)
    return teachers_cha

def see_groups(groups):
    if groups is None:
        print("Групп нет.")
    elif groups is empty:
        print("Групп нет.")
    else: 
        for i in range(0,len(groups)):
            print(f"{i+1}) {groups[i].get_number()}")

def add_group(groups):
    print("Введите номер группы.")
    gr_num = int(input())
    new_gr = UniversityClass(gr_num)
    groups_cha = groups.copy()
    groups_cha.append(new_gr)
    return groups_cha

def add_student_in_groups(students, groups):
    see_groups(groups)
    print("\nВведите порядковый номер, куда хотите добавить студентов.")
    gr_num = int(input()) - 1
    normal_output(1, all_stud_name(students))
    print("\nВведите порядковый номер студента, которого хотите добавить в группу.")
    st_num = int(input()) - 1
    groups_cha = groups.copy()
    groups_cha[gr_num].add_student(students[st_num])
    return groups_cha

def add_lesson(teachers, groups, lessons):
    normal_output(2, all_stud_name(teachers))
    print("\nВведите порядковый номер учителя, которому хотите назначить занятие.")
    teach_num = int(input()) - 1
    see_groups(groups)
    print("\nВведите порядковый номер группы, которой хотите назначить занятие.")
    group_num = int(input()) - 1
    print("Введите номер кабинета.")
    clarom_num = int(input())
    lessons_cha = lessons.copy()
    lessons_cha.append(Lesson(clarom_num, teachers[teach_num], groups[group_num]))
    return lessons_cha

def add_mark_in_student(students):
    normal_output(1, all_stud_name(students))
    print("\nВведите порядковый номер студента, которому хотите поставить оценку.")
    st_num = int(input()) - 1
    print("\nВведите оценку.")
    mark = int(input())
    student_cha = students.copy()
    student_cha[st_num].add_marks(mark)
    return student_cha
    

def see_marks(students):
    normal_output(1, all_stud_name(students))
    print("\nВведите порядковый номер студента, чьи оценки хотите посмотреть.")
    st_num = int(input()) - 1
    marks = []
    for i in range(0,len(students[st_num].get_marks())):
        marks.append(students[st_num].get_marks()[i])
    return marks

persons,teachers,students = hello()
groups = []
lessons = []

comand_i = 1
while comand_i != 0:
    print(
    f"\n-----------------------{comand_i}-----------------------\n"+
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
    "10) Посмотреть оценки студентов.\n"+
    "11) Копия студента."
    f"\n-----------------------{comand_i}-----------------------\n")
    choise = int(input())
    match choise:
        case 0: 
            print("До свидания!")
            comand_i = 0
        case 1: 
            normal_output(1, all_stud_name(students))
        case 2: 
            normal_output(2, all_teach_name(teachers))
        case 3: 
            students = add_student(students)
        case 4: 
            teachers = add_student(teachers)
        case 5: 
            see_groups(groups)
        case 6: 
            groups = add_group(groups)
        case 7: 
            groups = add_student_in_groups(students, groups)
        case 8: 
            lessons = add_lesson(teachers, groups)
        case 9: 
            students = add_mark_in_student(students)
        case 10: 
            print(see_marks(students))
        case 11: 
            print(copy.deepcopy(students[0]))
        case _: 
            print("Неизвестная команда!")
            comand_i = 0
    comand_i+=1

# 1) Вычисления - крутишь сколько угодно, ничего не меняется.
# 2) Действия - изменения происходят, когда производишь.
# 3) Вычисления и действия в разных функциях.
# 4) Ничего не должно меняться без ретурна и существовать вне функции одновременно.
# 5) Глобальные переменные - плохо. Появляться в функциях должно то, что есть в аргументах. 