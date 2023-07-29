class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def description(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

class Employee(Person):
    def __init__(self, name, age, salary, seniority): # Incluimos los parámetros name y age para que puedan satisfacer al constructor de la clase Person
        super().__init__(name, age) # Llamamos al constructor de la clase Person
        self.__salary = salary
        self.__seniority = seniority
    def description(self): # Sobrescribimos este método
        super().description() # Llamamos a este mismo método, pero el que está no aquí si no en la clase Person
        print(f'Salary: {self.__salary}, Seniority: {self.__seniority}') # Funcionalidad adicional

# Ejemplo de uso:
alice = Person("Alice", 30)
alice.description()

bob = Employee("Bob", 35, 50000, 5)
bob.description()

print(isinstance(bob, Employee)) # 'isinstance' devuelve True o False si un objeto es instancia de una clase que se especifica en el segundo parámetro
print(isinstance(alice, Employee))
