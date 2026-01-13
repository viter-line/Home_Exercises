# Завдання 1. Простий клас

# Створи клас Person, який має:

# атрибути:

# name

# age

# метод say_hello(), який виводить:

# Привіт, мене звати <name>, мені <age> років


# 👉 Створи об’єкт цього класу і виклич метод.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років")

p1 = Person("Andrii", 36)
p2 = Person("Oleksa", 22)
# print(p1)

p1.say_hello()
p2.say_hello()