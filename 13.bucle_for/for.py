for num in range(5): # 'num' toma el valor actual del rango. Por cada ciclo, 'num' va en aumento
	print(num)

print('\n')

find = 3
for num in range(10):
	print(num)
	if num == find:
		print('\n', num, ' found')
		break # Si ya lo encontró, podemos detenr la ejecución del for y ahorrar recursos

print('\n')

find = 15
for num in range(10):
	print(num)
	if num == find:
		print('\n', num, ' found')
		break # Si ya lo encontró, podemos detenr la ejecución del for y ahorrar recursos
else:
	print('Not found')

for char in "Legato": # 'Legato' es un iterable de caracteres, por eso es prefectamente recorrible
	print(char)