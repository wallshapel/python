point = { 'x': 25, 'y': 50 }
print(point) # Devuelve { 'x': 25, 'y': 50 }
print(*point) # Devuelve x y

print(point['x']) # Accedemos al valor que corresponde a la llave 'x'
print(point['y']) # Accedemos al valor que corresponde a la llave 'y'

point['y'] = 45 # Modificamos el valor de la llave 'y'
print(point)

point['z'] = 100 # Agregamos una nueva llave. Debe definirse el nombre de la llave y asignarsele un valor
print(point)

# Buscar una llave en un diccionario
if 'lala' in point: # Como la llave 'lala' no existe en el diccionario 'point' la línea siguiente no se ejecutará
	print('Found') 

print(point.get('lala', 'Not found')) # Forma abreviada de buscar una llave y establecer un valor o un texto por defecto en caso que no la encuentre

# Eliminar una llave
del(point['z'])
print(point)

# Recorrer un diccionario
for value in point.items():
	print(value) # Devuelve las llaves y sus valores en tuplas


users = [
	{'id': 1, 'name': 'Legato'},
	{'id': 2, 'name': 'Jason'},
	{'id': 3, 'name': 'Bruce'},
	{'id': 4, 'name': 'Beethoven'},
	{'id': 5, 'name': 'Liszt'},
	{'id': 6, 'name': 'Chopin'},
]

for user in users:
	print(user['name']) # Devuelve todos los 'name' de la lista

