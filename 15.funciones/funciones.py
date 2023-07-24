def hello(): # Declaramos una función llamada hello
	print('Hello world') # La función solo imprime un texto

hello() # Ejecutamos la función hello

def hello2(message): # Función como parámetro
	print(message)

hello2('Hello Legato') # Llamamos a la función y le pasamos el argumento

def default(name, surname = 'Bluesummers'): # Si no se pasa un segundo parámetro, este tomará por defecto el valor de 'Bluesummers'
	print(f'{name} {surname}')

default('Legato') # Devuelve Legato Bluesummers

def animal(name, state):
	print(f'{name} {state}')

animal(state = 'feliz', name = 'Chanchito') # A esto se le llama función con parámetros nombrados, si no se sabe cual es el orden de los parámetros, se pueden especificar en el llamado de la función, pero obligatoriamente toca hacer con todos los parámetros

def sum(*numbers): # *numbers es un parámetro iterable, por lo q se puede recorrer con un for o un while
	total = 0
	for num in numbers:
		total += num
	print(total)

sum(1, 2, 3, 4, 5) # Podemos pasar todos los argumentos que querramos
sum(40, 50) # No tienen que ser siempre el mismo número de argumentos

def get_products(**data): #**data es un parámetro de tipo diccionario
	print(data) # Accedemos a todos los parámetros dentro de 'data'
	print(data['name']) #Accedenis solo al aprámetro 'name' dentro de 'data'

get_products(id=1, name='piano')

def multiply(*numbers):
	total = 1
	for num in numbers:
		total *= num
	return total # Esta función devuelve el total de la multipicación

print(multiply(1, 2, 3, 4, 5))