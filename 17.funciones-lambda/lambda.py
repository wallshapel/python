# Estructura de definición: nombre_de_variable = argumentos : una sola instrucción
# Estructura de llamado: nombre_de_variable(argumentos)

sum = lambda a, b : a + b # Esta función recibe 2 parámetros, a y b y lo que hace es sumarlos. el resultado se lo asigna a una variable llamada sum
print(sum(2, 2)) # 4

greet = lambda name : f'Hello {name}!'
print(greet('Legato'))

higher = lambda a, b, c : f'The highest between {a}, {b}, {c} is {max(a, b, c)}'
print(higher(1, 2, 3))

def put_prefix(prefix):
	return lambda name : f'{prefix} {name}'

print(put_prefix('Sr')('Legato'))



users = [
	['Chanchito', 41],
	['Felipe', 1],
	['butterfly', 5]
]

users.sort(key = lambda element : element[1]) # 'key' es uin argumento propio de la función 'sort()'
print(users) # Ordena el listado ascendentemente por el campo numérico

users.sort(key = lambda element : element[1], reverse = True)
print(users) # Ordena el listado descendentemente por el campo numérico