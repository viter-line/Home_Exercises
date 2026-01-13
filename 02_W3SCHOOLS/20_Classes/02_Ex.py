# Завдання 2. Клас з логікою

# Створи клас Rectangle, який має:

# атрибути:

# width

# height

# метод area() — повертає площу прямокутника

# метод perimeter() — повертає периметр

# 👉 Створи прямокутник 5×3 і виведи:

# площу

# периметр

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def are(self):
        print('Are = ', self.width * self.height)
    
    def perimeter(self):
        print('Perimetr = ', self.width*2 + self.height*2)

o1 = Rectangle(10, 12)
o2 = Rectangle(15, 25)

o1.are()
o1.perimeter()

o2.are()
o2.perimeter()
