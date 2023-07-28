# Usando funciones
def generate_pairs(limit):
	num = 1
	list = []
	while num <= limit:
		list.append(num * 2)
		num += 1
	return list

print(generate_pairs(10)) # Obtenemos los 10 primeros pares inmediatamente

# Usando generadores
def generate_pairs2(limit):
	num = 1
	while num <= limit:
		yield num * 2 # Esto es lo que se devuelve por cada llamada. Equivale al clásico return
		num += 1

return_pairs = generate_pairs2(10)

print(next(return_pairs)) # Devuelve el primer par

print('Aquí podrían ir miles de líneas de código')

print(next(return_pairs)) # Devuelve el segundo par

print('Aquí podrían ir miles de líneas de código')

print(next(return_pairs)) # Devuelve el tercer par

# O sea, vamos obteniendo los pares a medida que los vayamos necesitando


def return_cities(*cities):
	for city in cities:
		yield from city # Con from indicamos que city también puede ser iterable

returned_cities = return_cities(['Berlín', 'Hamburgo'], ['Bogotá', 'Barranquilla'], ['New York', 'Texas'], ['LR', 'Agosto'], ['Moscú', 'Saint Petersburg'])

# Devolvemos los 2 primeros elementos del primer elemento sin necesidad de usar for anidados
print(next(returned_cities))
print(next(returned_cities))
print(next(returned_cities))
print(next(returned_cities))