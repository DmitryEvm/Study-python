
# 1. класс "Apple" с 4-мя переменными
class Apple:
    def __init__(self, w, r, c, v):
        self.weight = w
        self.ripeness = r
        self.color = c
        self.variety = v


ap1 = Apple(330, 75, 'red', 'red prince')
print(ap1.variety)
print('-----------')

# 2. метод для вычисления площади круга
class Circle:
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        import math
        return math.pi * self.radius**2


some_circle = Circle(20)
print(f'радиус круга: {some_circle.radius}см.')
print(f'площадь круга: {some_circle.area():.2f}см.')
print('-----------')


# 3. класс Person, по умолчанию квалификация = 1. + метод с выводом всей информации
class Person:
    def __init__(self, name, surname, qual=1):
        self.name = name
        self.surname = surname
        self.qual = qual

    def all_inf(self):
        print(f'Имя: {self.name}, Фамилия: {self.surname}, Квалификация: {self.qual}')


employee_01 = Person('Dmitry', 'Evmenov')
print(employee_01.name)
employee_01.all_inf()
print('-----------')


# 4. класс Triangle с методом нахождения площади
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        import math
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


some_triangle = Triangle(15, 18, 25)
print(f'Стороны треугольника: {some_triangle.a}, {some_triangle.b}, {some_triangle.c} см')
print(f'площадь треугольника: {some_triangle.area():.2f} см')
print('-----------')


# 5,6 классы Rectangle и Square. вычисление периметра. + в Square метод меняющий длину сторон
class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2 if self.b else self.a * 4


class Square(Rectangle):
    def change_size(self, add):
        self.b = None
        self.a = self.a + add


some_rectangle = Rectangle(10, 15)
print(f'стороны прямоугольника: {some_rectangle.a}, {some_rectangle.b}')
print(f'периметр прямоугольника: {some_rectangle.calculate_perimeter()}')
print()

some_square = Square(10, 20)
print(f'стороны квадрата: {some_square.a}')
print(f'периметр квадрата: {some_square.calculate_perimeter()}')
print()

some_square.change_size(5)
print(f'стороны квадрата: {some_square.a}')
print(f'периметр квадрата: {some_square.calculate_perimeter()}')
print()

some_square.change_size(-10)
print(f'стороны квадрата: {some_square.a}')
print(f'периметр квадрата: {some_square.calculate_perimeter()}')
print('-----------')


# курсы валют по отношению к 1BYN на сегодняшнюю дату
base_url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"


def get_cur():
    import requests
    url = base_url
    response = requests.get(url).json()
    for p in list(response):
        cur = p['Cur_OfficialRate']
        cur = '1 BYN - ' + (str(cur)) + " " + p['Cur_Abbreviation']
        print(cur)


print('Курс валют на сегодня:')
get_cur()
