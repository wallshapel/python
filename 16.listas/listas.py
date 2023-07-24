numbers = [1, 2, 3]
leters = ['a', 'b', 'c', 'd']
words = ['canchito', 'feliz']
booleans = [True, False, False, True]

print(booleans)

matrix = [[0, 1], [1, 0]]
print(matrix)

zeros = [0] * 10 # Replica 10 veces el elemento '0' dentro del listado
print(zeros)

alphanumeric = numbers + leters # Unimos dos listados
print(alphanumeric)

rango = list(range(1, 10)) # Creamos un listado con números del 1 al 10
print(rango)

chars = list('hello world') # Creamos un listado con cada una de las letras de la cadena 'hello world'

animals = ['frog', 'cat', 'dog', 'fish', 'bird']
print(animals[0 : 3]) # Devuelve los 3 primeros elementos de 'animals'
print(animals[::2]) # Devuelve los elementos cuyos índices sean solo pares y cero
print(animals[1::3]) # Devuelve los elementos desde el índice 1 y el que venga después de 3 índices desde alló

# Desempaquetado de listas

numbers = [1, 2, 3, 4, 5, 6]
first, second, third, fourth, fifth, sixth = numbers # Cada una de las variables de la izquierda, se le asigna un valor del listado. la cantidad de variables y de elementos deben coincidir
print(first, second, third, fourth, fifth, sixth) # Devuelve cada uno de los elementos del listado

first, *others = numbers # Si necesitamos recuperar y asignar a una variable solo el primer elemento, esta es la forma
print(first) # Devuelve solo el primer elemento

first, second, *others = numbers # Recuperamos el primer y segundo elemento en variables individuales
print(first, second) 

first, *others, last = numbers # Recupera en variables individuales el primer y último elemento
print(first, last)


for animal in enumerate(animals): # Obtener el índice de los elementos de una lista
	print(animal) # Devuelve una tupla. en el primer índice van los índices del listado, en el segundo índice, van los elementos del listado

# Las tuplas también son iterables de modo que se pueden desempaquetar
for index, animal in enumerate(animals):
	print(index)

# Buscar elementos en una lista
print(animals.index('bird')) # Devuelve 4 que es el índice donde está ubicado. Si el elemento a buscar no se encuentra en la lista devuelve un error
# una forma de solucionarlo es
if 'birds' in animals: # Nunca entrará aquí porque el elemento buscado no existe en la lista, pero nos ahorra el error
	print(animals.index('birds'))

# Buscar número de apariciones de un elemento en una lista
animals = ['frog', 'cat', 'dog', 'fish', 'bird', 'fish']
print(animals.count('fishs')) # devuelve 2 apariciones. Si el elemento buscado no se encuentra en la lista, devuelve 0

#Agregar elemento a la lista
animals.insert(5, 'rabit') # Agrega en el índice 5 a 'rabit'. Si el índice excede el tamaño de la lista, lo agrega de último, si es negativo, lo agrega al comienzo
print(animals)

animals.append('rat') # Agrega a 'rat' al final 
print(animals)

animals.remove('fish') # Elimina la primera aparición de un elemento en la lista
print(animals)

animals.pop() # Elimina el último elemento de la lista
print(animals)

animals.pop(1) # Elimina el elemento en el índice 1 de la lista
print(animals)

del animals[2] # Elimina el índice 2 de la lista
print(animals)

animals.clear() # Elimina todos los elementos de la lista
print(animals)

# Ordenamientos
numbers = [5, 22, 13, 4, 55, 16, 47, 98]
numbers.sort() # Devuelve la lista en orden ascendente
print(numbers)

numbers.sort(reverse = True) # Ordena la lista en orden descendente
print(numbers)

numbers_copy = sorted(numbers) # Devuelve una lista ordenada ascendentemente de la lista
print(numbers_copy)

numbers_copy = sorted(numbers, reverse = True) # Devuelve una lista ordenada descendentemente de la lista
print(numbers_copy)

users = [
	['Chanchito', 41],
	['Felipe', 1],
	['butterfly', 5]
]

users.sort() # No lo ordena debido a que los índices no están de primero
print(users)

def order(element):
	return element[1] # Retornamos lo que nos pasen en el índice 1 y no el cero

users.sort(key = order)
print(users) # ahora sí ordena los usuarios por el campo numérico