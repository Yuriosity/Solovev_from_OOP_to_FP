from random import randint, randrange


import random
import string
from turtle import pen

from person import Person
from student import Student
from teacher import Teacher


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

generator = []
i = 0
while i < 30:
    random_age = randint(18,80)
    random_name = generate_random_string(randint(5,10))
    generator.append(random_name + "; " + str(random_age) + "; " + str(generate_random_string(randint(1,3))))
    i+=1

f = open('generator.txt', 'w')
for index in generator:
    f.write(index + '\n')
f.close()
