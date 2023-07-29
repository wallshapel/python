import math

class Figure(): # Clase abstracta 'Figure'
    def calculate_area(self):
        pass

class Circle(Figure): # Clase Circle que hereda de Figure
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure): # Clase Triangle que hereda de Figure
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def calculate_area(self):
        return (self.__base * self.__height) / 2

# Ejemplo de uso
circle = Circle(5)
triangle = Triangle(8, 4)

print('Circle area:', circle.calculate_area())  # Salida: Área del círculo: 78.54
print('Triangle area:', triangle.calculate_area())  # Salida: Área del triángulo: 16.0
